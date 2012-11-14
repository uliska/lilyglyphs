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

import lilyglyphs_common as lg, os, sys, getopt
from __commands import *
from __strings import *

# Global variables

commands = None

def main(argv):
    global commands
    short_options = 'i:'
    long_options = []
    long_options.append('input=')
    try:
        opts, args = getopt.getopt(argv, short_options, long_options)
        for opt, arg in opts:
            if opt in ("-i",  "--input"):
                # Create commands object, load file and parse entries
                commands = ImageCommands(arg)
            else:
                usage()
                sys.exit(2)
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    # TODO: list existing src files, check for duplicates

    # TODO: check for definition of already existing commands
    # (for now ignore that, maybe add an option to refuse the re-creation)

    print ''
    write_lily_src_files()

    print commands
    for cmd in commands:
        print cmd
    print ''
    lg.compile_lily_files(commands)

    # update to use new dict
    print ''
    #lg.generate_latex_commands()

    # check, should still work
    print ''
    lg.cleanup_lily_files()

    print ''
    #write_latex_file()


def check_paths():
    """Sets CWD to 'glyphimages' subdir
       and makes sure that the necessary subdirectories are present"""
    global lilyglyphs_root
    lg.check_lilyglyphs_root()
    os.chdir('glyphimages')

    # check the presence of the necessary subdirectories
    # and create them if necessary
    # (otherwise we'll get errors when trying to write in them)
    ls = os.listdir('.')
    if not os.path.exists(lg.dir_lysrc):
        os.mkdir(dir_lysrc)
    if not os.path.exists(lg.dir_pdfs):
        os.mkdir('pdfs')
    if not os.path.exists(lg.dir_stash):
        os.mkdir(lg.dir_stash)
    if not os.path.exists(lg.dir_stash + 'images'):
        os.mkdir(lg.dir_stash + 'images')

def usage():
    print """build-image-commands. Part of the lilyglyphs package.
    Parses a lilyglyphs source file, creates
    single .ly files from it, uses LilyPond to create single glyph
    pdf files and set up template commands to be used in LaTeX.
    For detailed instructions refer to the manual.
    Usage:
    -i filename --input=filename (mandatory): Specifies the input file.

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
    fout.write(lg.signature())
    fout.write('\n\n')


def write_latex_file():
    """Composes LaTeX file and writes it to disk"""
    print 'Generate LaTeX file'
    lg.write_latex_file('images/newImageGlyphs.tex')


def write_lily_src_files():
    """Generates one .ly file for each found new command"""
    print 'Write .ly files for each entry:'

    src_dir = os.path.join(d_src, commands.cat_subdir)
    if not os.path.exists(src_dir):
        os.mkdir(src_dir)

    for cmd in commands:
        cmd_name = cmd.name
        print '- ' + cmd_name
        # open a single lily src file for write access
        fout = open(os.path.join(src_dir, cmd_name + '.ly'), 'w')

        #output the license information
        fout.write(lg.lilyglyphs_copyright_string)
        fout.write('\n')

        #output information on the actual file
        write_file_info(cmd_name, fout)

        #write the default LilyPond stuff
        fout.write(lily_src_prefix)

        # write the comment for the command
        fout.write('%{\n')
        for line in cmd.comment:
            fout.write(line + '\n')
        fout.write('%}\n\n')

        # write the actual command
        fout.write(cmd_name + ' = {\n')
        for line in cmd.lilySrc:
            fout.write(line + '\n')
        fout.write('}\n')

        # write the score definition
        fout.write(lily_src_score)

        # finish the LilyPond file
        fout.write('  \\' + cmd_name + '\n')
        fout.write('}\n\n')

        fout.close()


# ####################################
# Finally launch the program
if __name__ == "__main__":
    print 'build-image-commands.py,'
    print 'Part of lilyglyphs.'

    check_paths()
    main(sys.argv[1:])
