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

import os, sys, datetime

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

# LilyPond commands
in_cmds = {}
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
cmd_templates = {}
cmd_templates['image'] = """\\newcommand*{\\CMDBase}[1][]{%
    \\setkeys{lilyDesignOptions}{scale=1,raise=0}%
    \\lilyPrintImage[#1]{CMD}%
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

def cleanup_lily_files():
    """Removes unneccessary files from LilyPond compilation,
    rename and remove the preview PDF files to the right directory."""
    #dir_in = out_lysrc + '/'
    #dir_out = out_images + '/'
    file_list = os.listdir(dir_lysrc)

    print 'Remove intermediate files'
    for file in file_list:
        dummy, extension = os.path.splitext(file)
        if not extension in ['.pdf', '.ly']:
            os.remove(dir_lysrc + file)

    print 'Clean up:'
    for cmd_name in in_cmds:
        print '- ' + cmd_name
        # remove full-page pdf
        os.remove(dir_lysrc + cmd_name + '.pdf')
        # rename/move small 'preview' pdf
        os.rename(dir_lysrc + cmd_name + '.preview.pdf',  dir_pdfs + cmd_name + '.pdf')

def generate_latex_command(cmd_name, cmd_type):
    """Writes templates for the commands in a new LaTeX file.
    These should manually be moved to the appropriate .inp files
    in lilyglyphs"""

    latex_cmds[cmd_name] = []

    # create LaTeX command
    cmd = []
    cmd.append('% ' + str(in_cmds[cmd_name][0])[2:-2] + '\n')
    cmd.append(signature() + '\n')
    cmd.append(cmd_templates[cmd_type].replace('CMD', cmd_name))
    latex_cmds[cmd_name].append(cmd)

    # create documentation table

    # create LaTeX test code
    tc = []
    tc.append(testcode_template.replace('CMD', cmd_name))
    latex_cmds[cmd_name].append(tc)


def read_input_file(in_file):
    """Reads the input source file and stores it"""
    global definitions_file

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
    fout.write('% New Image Glyphs for the lilyglyphs package\n')
    fout.write(signature() + '\n')
    fout.write(latexfile_start_comment.replace('SCRIPT_NAME', script_name()))

    # write out command definitions
    for cmd_name in latex_cmds:
        for line in latex_cmds[cmd_name][0]:
            fout.write(line)

    fout.write(latexfile_begin_document)
    fout.write(signature()[2:]+ '\n')
    fout.write(latexfile_reftable)

    # write out the reference table
    row_template = '\\CMD & \\cmd{CMD} & description\\\\'
    for cmd_name in latex_cmds:
        fout.write(row_template.replace('CMD', cmd_name) + '\n')
    fout.write(latexfile_testcode)

    # write out the test code
    for cmd_name in latex_cmds:
        for line in latex_cmds[cmd_name][1]:
            fout.write(line)

    fout.write('\\end{document}\n')
    fout.close()


