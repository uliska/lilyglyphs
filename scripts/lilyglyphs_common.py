#!/usr/bin/env python

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                                                                        %
#      This file is part of the 'lilyglyphs' LaTeX package.              %
#                                ==========                              %
#                                                                        %
#              https://github.com/openlilylib/lilyglyphs                 %
#               http://www.openlilylib.org/lilyglyphs                    %
#                                                                        %
#  Copyright 2012-2013 Urs Liska and others, ul@openlilylib.org          %
#                                                                        %
#  'lilyglyphs' is free software: you can redistribute it and/or modify  %
#  it under the terms of the LaTeX Project Public License, either        %
#  version 1.3 of this license or (at your option) any later version.    %
#  You may find the latest version of this license at                    %
#               http://www.latex-project.org/lppl.txt                    %
#  more information on                                                   %
#               http://latex-project.org/lppl/                           %
#  and version 1.3 or later is part of all distributions of LaTeX        %
#  version 2005/12/01 or later.                                          %
#                                                                        %
#  This work has the LPPL maintenance status 'maintained'.               %
#  The Current Maintainer of this work is Urs Liska (see above).         %
#                                                                        %
#  This work consists of the files listed in the file 'manifest.txt'     %
#  which can be found in the 'license' directory.                        %
#                                                                        %
#  This program is distributed in the hope that it will be useful,       %
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        %
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  %
#                                                                        %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ########################################################################
#                                                                        #
# lilyglyphs_common.py                                                   #
#                                                                        #
# Common functionality for the Python scripts in lilyglyphs              #
#                                                                        #
# ########################################################################

import os, sys, datetime, subprocess, argparse

# ################
# Global variables

definitions_file = []
version_string = '0.2.2'

# ######################
# Common CL arguments
common_arguments = argparse.ArgumentParser(add_help=False)
common_arguments.add_argument('-v', '--version', 
                               action='version', 
                               version='%(prog)s ' + version_string)

def is_file(filename):
    if os.path.exists(filename):
        return filename
    else:
        msg = "file %s not found" % filename
        raise argparse.ArgumentTypeError(msg)


# ###########
# Directories
dir_defs = 'definitions'
dir_lysrc = 'generated_src'
dir_pdfs = 'pdfs'
dir_cmd = 'generated_cmd'

# LilyPond commands
in_cmds = {}
# LilyPond source files (corresponds to in_cmds)
# stores basenames without path and extension
lily_files = []
# LaTeX commands
latex_cmds = {}

# #######
# Strings

lilyglyphs_copyright_string = """
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                        %
%      This file is part of the 'lilyglyphs' LaTeX package.              %
%                                ==========                              %
%                                                                        %
%              https://github.com/openlilylib/lilyglyphs                 %
%               http://www.openlilylib.org/lilyglyphs                    %
%                                                                        %
%  Copyright 2012-2013 Urs Liska and others, ul@openlilylib.org          %
%                                                                        %
%  'lilyglyphs' is free software: you can redistribute it and/or modify  %
%  it under the terms of the LaTeX Project Public License, either        %
%  version 1.3 of this license or (at your option) any later version.    %
%  You may find the latest version of this license at                    %
%               http://www.latex-project.org/lppl.txt                    %
%  more information on                                                   %
%               http://latex-project.org/lppl/                           %
%  and version 1.3 or later is part of all distributions of LaTeX        %
%  version 2005/12/01 or later.                                          %
%                                                                        %
%  This work has the LPPL maintenance status 'maintained'.               %
%  The Current Maintainer of this work is Urs Liska (see above).         %
%                                                                        %
%  This work consists of the files listed in the file 'manifest.txt'     %
%  which can be found in the 'license' directory.                        %
%                                                                        %
%  This program is distributed in the hope that it will be useful,       %
%  but WITHOUT ANY WARRANTY; without even the implied warranty of        %
%  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  %
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
sed \\CMD{} do eiusmod tempor incididunt ut labore et dolore magna aliqua \\CMD.\\\\
\\CMD{} Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur \\CMD.
\\CMD{} Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

\\bigskip
"""

# Default values for optional argument in generated commands
DEF_SCALE = '1'
DEF_RAISE = '0'

# template strings to build the command from
# 'CMD' will be replaced by the actual command_name
# 'ELEM' will be replaced by the actual content element to be rendered

cmd_templates = {}
cmd_templates['image'] = """\\newcommand*{\\CMD}[1][]{%
    \\setkeys{lilyDesignOptions}{scale=SCALE,raise=RAISE}%
    \\lilyPrintImage[#1]{ELEM}%
}

"""

cmd_templates['glyphname'] = """\\newcommand*{\\CMD}[1][]{%
	\\setkeys{lilyDesignOptions}{scale=SCALE,raise=RAISE}%
	\\lilyPrint[#1]{\\lilyGetGlyph{ELEM}}%
}

"""

cmd_templates['number'] = """\\newcommand*{\\CMD}[1][]{%
	\\setkeys{lilyDesignOptions}{scale=SCALE,raise=RAISE}%
	\\lilyPrint[#1]{\\lilyGetGlyphByNumber{ELEM}}%
}

"""

cmd_templates['dynamics'] = """\\newcommand{\\CMD}[1][]{%
	\\mbox{%
		\\lilyDynamics[#1]{ELEM}%
	}%
}

"""

cmd_templates['text'] = """\\newcommand{\\CMD}[1][]{%
	\\setkeys{lilyDesignOptions}{scale=SCALE,raise=RAISE}%
	\\mbox{%
		\\lilyText[#1]{ELEM}%
	}%
}

"""

def cleanup_lily_files():
    """Removes unneccessary files from LilyPond compilation,
    rename and remove the preview PDF files to the right directory."""

    print 'Clean up directories'
    
    # iterate through dir_lysrc
    os.chdir(dir_lysrc)
    for entry in os.listdir('.'):
        if os.path.isfile(entry):
            name, extension = os.path.splitext(entry)
            #remove unnecessary files
            if not extension in ['.pdf', '.ly']:
                os.remove(entry)
            if extension == '.pdf':
                # remove full-page pdf
                if '.preview' in name:
                    newfile = entry.replace('.preview.', '.')
                    newfile = os.path.join('..', dir_pdfs, newfile)
                    # rename/move small 'preview' pdf
                    os.rename(entry, newfile)
                else:
                    os.remove(entry)                    
    os.chdir('..')
    
def compile_lily_files():
    """Compiles LilyPond files to """
    print 'Compile with LilyPond:'
    for file in lily_files:
        args = []
        args.append("lilypond")
        args.append("-o")
        args.append(dir_lysrc)
        args.append("-dpreview")
        args.append("-dno-point-and-click")
        args.append(os.path.join(dir_lysrc, file + ".ly"))
        subprocess.call(args)
        print ''

def generate_latex_commands():
    """Generates the templates for the commands in a new LaTeX file.
    These should manually be moved to the appropriate .inp files
    in lilyglyphs"""

    # iterate over the list of commands
    for cmd_name in in_cmds:
        latex_cmds[cmd_name] = {}

        # create LaTeX command
        cmd = []
        for line in in_cmds[cmd_name]['comment']:
            cmd.append('% ' + line + '\n')
        cmd.append(signature() + '\n')
        template = cmd_templates[in_cmds[cmd_name]['type']]
        template = template.replace('CMD', cmd_name)
        if 'scale' in in_cmds[cmd_name]:
            scale = in_cmds[cmd_name]['scale']
        else:
            scale = DEF_SCALE
        template = template.replace('SCALE', scale)
        if 'raise' in in_cmds[cmd_name]:
            rais = in_cmds[cmd_name]['raise']
        else:
            rais = DEF_RAISE
        template = template.replace('RAISE', rais)
        cmd.append(template.replace('ELEM', in_cmds[cmd_name]['element']))
        latex_cmds[cmd_name]['cmd'] = cmd
    
        # create LaTeX test code
        tc = []
        tc.append(testcode_template.replace('CMD', cmd_name))
        latex_cmds[cmd_name]['testcode'] = tc

def read_input_file(in_file):
    """Reads the input source file and stores it 
    in the global variable definitions_file"""
    global definitions_file
    
    in_file = os.path.normpath(in_file)

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
    fout = open(file_name, 'w')
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
