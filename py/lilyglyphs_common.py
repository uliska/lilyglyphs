#!/usr/bin/env python

# ########################################################################
#                                                                        #
#      This file is part of the 'lilyglyphs' LaTeX package.              #
#                                ==========                              #
#                                                                        #
#              https://github.com/uliska/lilyglyphs                      #
#                                                                        #
#  Copyright 2012 by Urs Liska, git@ursliska.de                          #
#                                                                        #
#  'lilyglyphs' is free software: you can redistribute it and/or modify  #
#  it under the terms of the GNU General Public License as published by  #
#  the Free Software Foundation, either version 3 of the License, or     #
#  (at your option) any later version.                                   #
#                                                                        #
#  This program is distributed in the hope that it will be useful,       #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          #
#  GNU General Public License for more details.                          #
#                                                                        #
#  You should have received a copy of the GNU General Public License     #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#                                                                        #
# ########################################################################

# ########################################################################
#                                                                        #
# lilyglyphs_common.py                                                   #
#                                                                        #
# Common functionality for the Python scripts in lilyglyphs              #
#                                                                        #
# ########################################################################

import os, sys, datetime, subprocess

# ################
# Global variables

definitions_file = []

# ###########
# Directories
lilyglyphs_root = ''

dir_defs = 'definitions/'
dir_lysrc = 'generated_src/'
dir_pdfs = 'pdfs/'
dir_stash = 'stash_new_commands/'
# subdirectory to save the lily sources and the pdf to
cat_subdir = ''

# LilyPond commands
in_cmds = {}
# LilyPond source files (corresponds to in_cmds)
# list of tuples (cat_subdir, name)
lily_files = []
# LaTeX commands
latex_cmds = {}

# files with the glyph definitions
input_files = []

# #######
# Strings

lilyglyphs_copyright_string = """
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                        %
%      This file is part of the 'lilyglyphs' LaTeX package.              %
%                                ==========                              %
%                                                                        %
%              https://github.com/uliska/lilyglyphs                      %
%                                                                        %
%  Copyright 2012 by Urs Liska, git@ursliska.de                          %
%                                                                        %
%  'lilyglyphs' is free software: you can redistribute it and/or modify  %
%  it under the terms of the GNU General Public License as published by  %
%  the Free Software Foundation, either version 3 of the License, or     %
%  (at your option) any later version.                                   %
%                                                                        %
%  This program is distributed in the hope that it will be useful,       %
%  but WITHOUT ANY WARRANTY; without even the implied warranty of        %
%  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          %
%  GNU General Public License for more details.                          %
%                                                                        %
%  You should have received a copy of the GNU General Public License     %
%  along with this program.  If not, see <http://www.gnu.org/licenses/>. %
%                                                                        %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

latexfile_start_comment = """
% This file contains definitions for the new commands
% along with test code for them.
% You can test the commands in the context of continuous text
% and adjust their design time options.
% Afterwards you should manually move the commands to
% the appropriate .inp files,
% because this file will be overwritten by the next run
% of SCRIPT_NAME!
% If you want to keep this file for reference
% you should save it with a new name.
%
% There also is a table containing entries for use in the lilyglyph manual.
% You can either copy the whole table to the appropriate
% place in lilyglyphs.tex or just copy individual table rows.

\\documentclass{scrartcl}
\\usepackage{lilyglyphsStyle}

%%%%%%%%%%%%%%%%%%%%%%%%%
% new command definitions

"""

latexfile_begin_document = """

\\begin{document}

%%%%%%%%%%%%%
% Text output

\\section*{New \\lilyglyphs{} commands}
"""

latexfile_reftable = """
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Reference table to be used in the manual
% (use complete or single lines)

\\begin{reftable}{New commands}{newcommands}
"""

latexfile_testcode = """\\end{reftable}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Test code for fine-tuning the new commands
"""

# ##############
# Code templates

# template string to build the test code for the commands
# 'CMD' will be replaced by the actual command_name
testcode_template = """

\\noindent\\textbf{\\textsf{Continuous text for} \\cmd{CMD}:}\\\\
Lorem ipsum dolor sit amet, consectetur adipisicing elit,
sed \\CMD do eiusmod tempor incididunt ut labore et dolore magna aliqua \\CMD*.\\\\
\\CMD Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur\\CMD.
\\CMD Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

\\bigskip
"""


# template strings to build the command from
# 'CMD' will be replaced by the actual command_name
# 'ELEM' will be replaced by the actual content element to be rendered

cmd_templates = {}
cmd_templates['image'] = """\\newcommand*{\\CMDBase}[1][]{%
    \\setkeys{lilyDesignOptions}{scale=1,raise=0}%
    \\lilyPrintImage[#1]{ELEM}%
}
\\newcommand*{\\CMD}[1][]{\\CMDBase[#1] }
\\WithSuffix\\newcommand\\CMD*[1][]{\\CMDBase[#1]}

"""

cmd_templates['glyphname'] = """\\newcommand*{\\CMDBase}[1][]{%
	\\setkeys{lilyDesignOptions}{scale=1,raise=0}%
	\\lilyPrint[#1]{\\lilyGetGlyph{ELEM}}%
}
\\newcommand*{\\CMD}[1][]{\\CMDBase[#1] }
\\WithSuffix\\newcommand\\CMD*[1][]{\\CMDBase[#1]}

"""

cmd_templates['number'] = """\\newcommand*{\\CMDBase}[1][]{%
	\\setkeys{lilyDesignOptions}{scale=1,raise=0}%
	\\lilyPrint[#1]{\\lilyGetGlyphByNumber{ELEM}}%
}
\\newcommand*{\\CMD}[1][]{\\CMDBase[#1] }
\\WithSuffix\\newcommand\\CMD*[1][]{\\CMDBase[#1]}

"""

cmd_templates['dynamics'] = """\\newcommand{\\CMDBase}[1][]{%
	\\mbox{%
		\\lilyDynamics[#1]{ELEM}%
	}%
}
\\newcommand*{\\CMD}[1][]{\\CMDBase[#1] }
\\WithSuffix\\newcommand\\CMD*[1][]{\\CMDBase[#1]}

"""

cmd_templates['text'] = """\\newcommand{\\CMDBase}[1][]{%
	\\mbox{%
		\\lilyText[#1]{ELEM}%
	}%
}
\\newcommand*{\\CMD}[1][]{\\CMDBase[#1] }
\\WithSuffix\\newcommand\\CMD*[1][]{\\CMDBase[#1]}

"""

def check_lilyglyphs_root():
    """Checks if the current working directory
       is within the rootline of the lilyglyphs package.
       If this is the case it sets the cwd to be
       the root of the package."""
    global lilyglyphs_root, dir_stash

    print 'Checking directories'
    
    # check current working dir
    cwd = os.getcwd()
    if not 'lilyglyphs' in cwd:
        print 'Your current working directory seems to be wrong.'
        print 'Please cd to a location in the lilyglyphs directory.'
        sys.exit(2)

    # set global variable
    lilyglyphs_root = cwd[:cwd.find('lilyglyphs') + 11]
    dir_stash = lilyglyphs_root + 'stash_new_commands/'
    # set current working dir
    os.chdir(lilyglyphs_root)

def check_missing_pdfs():
    """Compares the list of LilyPond source and resulting PDF files.
       Returns a list of LilyPond source file names (without folder)
       which don't have a corresponding PDF file"""
    print 'Reading file lists, counting missing pdf files'
    img_files = []
    for entry in os.listdir(dir_pdfs):
        out_dir = dir_pdfs + entry + '/'
        if os.path.isdir(out_dir):
            # read existing .pdf files in out_dir
            for file in os.listdir(out_dir):
                name,  ext = os.path.splitext(file)
                if ext == '.pdf':
                    img_files.append(name)

    # read existing .ly source files in in_dir
    # and add them to the sources list if the image is missing
    src_files = []
    for entry in os.listdir(dir_lysrc):
        in_dir = dir_lysrc + entry + '/'
        if os.path.isdir(in_dir):
            for file in os.listdir(in_dir):
                name,  ext = os.path.splitext(file)
                if ext == '.ly' and name not in img_files:
                    src_files.append((entry + '/', name))
    return src_files

def cleanup_lily_files():
    """Removes unneccessary files from LilyPond compilation,
    rename and remove the preview PDF files to the right directory."""
    global cat_subdir
    
    print 'Clean up directories'
    
    # iterate through the subdirectories of dir_lysrc
    for entry in os.listdir(dir_lysrc):
        in_dir = dir_lysrc + entry + '/'
        if os.path.isdir(in_dir):
            # make sure there is a corresponding dir_pdfs directory
            out_dir = dir_pdfs + entry + '/'
            if not os.path.exists(out_dir):
                os.mkdir(out_dir)
            # iterate through the subdir
            for file in os.listdir(in_dir):
                name, extension = os.path.splitext(file)
                #remove unnecessary files
                if not extension in ['.pdf', '.ly']:
                    os.remove(in_dir + file)
                if extension == '.pdf':
                    # remove full-page pdf
                    if not '.preview' in name:
                        os.remove(in_dir + file)
                    else:
                        newfile = file.replace('.preview.', '.')
                        # rename/move small 'preview' pdf
                        os.rename(in_dir + file,  out_dir + newfile)
                    
        
def compile_lily_files():
    """Compiles LilyPond files to """
    print 'Compile with LilyPond:'
    for file in lily_files:
        args = []
        args.append("lilypond")
        args.append("-o")
        args.append(dir_lysrc + file[0])
        args.append("-dpreview")
        args.append("-dno-point-and-click")
        args.append(dir_lysrc + file[0] + file[1] + ".ly")
        subprocess.call(args)
        print ''

def generate_latex_commands():
    """Generates the templates for the commands in a new LaTeX file.
    These should manually be moved to the appropriate .inp files
    in lilyglyphs"""

    
    for cmd_name in in_cmds:
        latex_cmds[cmd_name] = {}

        # create LaTeX command
        cmd = []
        for line in in_cmds[cmd_name]['comment']:
            cmd.append('% ' + line + '\n')
        cmd.append(signature() + '\n')
        template = cmd_templates[in_cmds[cmd_name]['type']]
        templateCMD = template.replace('CMD', cmd_name)
        cmd.append(templateCMD.replace('ELEM', in_cmds[cmd_name]['element']))
        latex_cmds[cmd_name]['cmd'] = cmd
    
        # create documentation table
    
        # create LaTeX test code
        tc = []
        tc.append(testcode_template.replace('CMD', cmd_name))
        latex_cmds[cmd_name]['testcode'] = tc


def read_input_file(in_file):
    """Reads the input source file and stores it 
    in the global variable definitions_file"""
    global definitions_file

    print 'Read input file ' + in_file
    
    # check for existence of input file
    if not os.path.exists(in_file):
                    print 'File ' + in_file + ' not found.'
                    print 'Please specify an input file'
                    sys.exit(2)

    fin = open(in_file,  'r')
    for line in fin:
        definitions_file.append(line.rstrip(' \n'))
    fin.close()

def script_name():
    dummy, result = os.path.split(sys.argv[0])
    return result

def signature():
    """Returns a signature to be inserted in an output file"""
    return '% created by ' + script_name() + ' on ' + str(datetime.date.today())

def write_latex_file(file_name):
    fout = open(dir_stash + file_name, 'w')
    fout.write('% New Glyphs for the lilyglyphs package\n')
    fout.write(signature() + '\n')
    fout.write(latexfile_start_comment.replace('SCRIPT_NAME', script_name()))

    # write out command definitions
    sorted_cmds = sorted(latex_cmds.iterkeys())
    for cmd_name in sorted_cmds:
        for line in latex_cmds[cmd_name]['cmd']:
            fout.write(line)

    fout.write(latexfile_begin_document)
    fout.write(signature()[2:]+ '\n')
    fout.write(latexfile_reftable)

    # write out the reference table
    row_template = '\\CMD & \\cmd{CMD} & description\\\\'
    for cmd_name in sorted_cmds:
        fout.write(row_template.replace('CMD', cmd_name) + '\n')
    fout.write(latexfile_testcode)

    # write out the test code
    for cmd_name in sorted_cmds:
        for line in latex_cmds[cmd_name]['testcode']:
            fout.write(line)

    fout.write('\\end{document}\n')
    fout.close()


