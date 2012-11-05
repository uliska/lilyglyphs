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

import os,  sys,  getopt,  datetime

# ################
# Global variables

# flags
flag_force = False

# file with the glyph definitions
definitions_file_name = ''
definitions_file = []

# LilyPond commands
lily_cmds = {}


# ###############
# Used constants

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

# string to be printed before the actual command
lily_src_prefix = """\\version "2.17.4"

#(set-global-staff-size 14)

\paper {
  indent = 0
}
\header {
  tagline = ""
}

"""

# string to be printed after the actual command definition
lily_src_score = """
  \\score {
  \\new Staff \\with {
    \\remove "Staff_symbol_engraver"
    \\remove "Clef_engraver"
    \\remove "Time_signature_engraver"
  }
"""

def main(argv):
    global flag_force, definitions_file_name
    try:
        opts, args = getopt.getopt(argv, "i:f", ["input=","force"])
        for opt, arg in opts:
            if opt in ("-f",  "--force"):
                flag_force = True
            if opt in ("-i",  "--input"):
                definitions_file_name = arg
            else:
                usage()
                sys.exit(2)
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    # Do the actual work of the script
    print ''
    print 'buildImageGlyphs.py,'
    print 'Part of lilyglyphs.'

    print ''
    print 'Read file ' + definitions_file_name
    read_input_file()

    print ''
    print 'Read entries of LilyPond commands:'
    read_entries()

    print ''
    print 'Write .ly files for each entry:'
    write_lily_src_files()

    # compile lily-files
    # move lily-files
    # cleanup unused files
    # write LaTeX templates


def read_entries():
    """Parses the input source file and extracts glyph entries"""
    for i in range(len(definitions_file)):
        if '% lilyglyphs entry' in definitions_file[i]:
            read_entry(i)


def read_entry(i):
    """Reads a single glyph entry from the input file and stores it
    in the global dictionary lily_cmds"""
    global lily_cmds
    # read comment line(s)
    comment = []
    while True:
        i += 1
        cur_line = definitions_file[i].strip()
        first_line = cur_line.find('%{')
        if first_line >= 0:
            cur_line = cur_line[first_line + 3 :]
        last_line = cur_line.find('%}')
        if last_line >= 0:
            comment.append(cur_line[: last_line].strip())
            break
        else:
            comment.append(cur_line)
    i += 1
    # read command name
    cur_line = definitions_file[i].strip()
    command_name = cur_line[: cur_line.find('=') - 1]
    print '- ' + command_name
    # read actual command until we find a line the begins with a closing curly bracket
    i += 1
    lilySrc = []
    while definitions_file[i][0] != '}':
        lilySrc.append(definitions_file[i])
        i += 1
    lily_cmds[command_name] = [comment,  lilySrc]


def read_input_file():
    """Reads the input source file and stores it"""
    global definitions_file
    definitions_file = []
    fin = open('definitions/' + definitions_file_name,  'r')
    for line in fin:
        definitions_file.append(line.rstrip(' \n'))
    fin.close()

def usage():
    print """buildImageGlyphs. Part of the lilyglyphs package.
    Parses a .lysrc (lilyglyphs source) file, creates
    single .ly files from it, uses LilyPond to create single glyph
    pdf files and set up template files to be used in LaTeX.
    For detailed instructions refer to the manual.
    Usage:
    -i filename --input=filename (mandatory): Specifies the input file.
    -f --force: overwrite files if they already exist
    """

def write_file_info(name, fout):
    """Formats file specific information for the lilyPond source file"""
    long_line = '% This file defines a single glyph to be created with LilyPond: %\n'
    width = len(long_line) - 1
    header = '%' * width + '\n'
    spacer = '%' + ' ' * (width - 2) + '%\n'
    padding = width - len(name) - 8
    fout.write(header)
    fout.write(spacer)
    fout.write(long_line)
    fout.write(spacer)
    fout.write('%   ' + name + '.ly' + ' ' * padding + '%\n')
    fout.write(spacer)
    fout.write(header)
    fout.write('% created by buildImageGlyphs.py\n')
    fout.write('% on ' + str(datetime.date.today()))
    fout.write('\n\n')

def write_lily_src_files():
    for command_name in lily_cmds:
        print '- ' + command_name
        # open a single lily src file for write access
        fout = open('processed/' + command_name + '.ly',  'w')

        #output the license information
        fout.write(lilyglyphs_copyright_string)
        fout.write('\n')

        #output information on the actual file
        write_file_info(command_name, fout)

        #write the default LilyPond stuff
        fout.write(lily_src_prefix)

        # write the comment for the command
        fout.write('%{\n')
        for line in lily_cmds[command_name][0]:
            fout.write(line + '\n')
        fout.write('%}\n\n')

        # write the actual command
        fout.write(command_name + ' = {\n')
        for line in lily_cmds[command_name][1]:
            fout.write(line + '\n')
        fout.write('}\n')

        # write the score definition
        fout.write(lily_src_score)

        # finish the LilyPond file
        fout.write('  \\' + command_name + '\n')
        fout.write('}\n\n')

        fout.close()

# ####################################
# Finally launch the program
if __name__ == "__main__":
    main(sys.argv[1:])
