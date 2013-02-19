#!/usr/bin/env python

# ########################################################################
#                                                                        #
#      This file is part of the 'lilyglyphs' LaTeX package.              #
#                                ==========                              #
#                                                                        #
#              https://github.com/uliska/lilyglyphs                      #
#                                                                        #
#  Copyright 2012 by Urs Liska, lilyglyphs@ursliska.de                    #
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


import lib.common as common, lib.globals as globals
import lib, os, sys, getopt
from lib.inputfileimages import InputFileImages
from lib.latexcommand import LatexCommand

from lib.latexfile import LatexFile
from lib.lilyfile import LilypondFile


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
                def_file = InputFileImages(arg)

                # load file from disk
                def_file.load()

                # parse the file and generate the Commands entries
                def_file.read_entries()

                # generate the contents of a LaTeX file from the Command entries.
                def_file.generate_latex_file()

                # write out the LaTeX file to disk
                def_file.write_latex_file()



            else:
                usage()
                sys.exit(2)
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    # TODO: list existing src files, check for duplicates

    # TODO: check for definition of already existing commands
    # (for now ignore that, maybe add an option to refuse the re-creation)

    # generate new LilyPond source files
    commands.write_lily_src_files()

    # Compile all new LilyPond files
    commands.compile_lily_files()


    # create a LatexFile instance and write the result file
    LatexFile(commands).write()


    # clean up the source folder and
    # move the created image to the img folder
    common.cleanup_lily_files()

    # End of the program


def check_paths():
    """Sets CWD to globals.GLYPH_IMG_ROOT subdir of lilyglyphs root
       and makes sure that the necessary subdirectories are present"""
    common.check_lilyglyphs_root(globals.GLYPH_IMG_ROOT)

    # check the presence of the necessary subdirectories
    # and create them if necessary
    # (otherwise we'll get errors when trying to write in them)
    if not os.path.exists(globals.D_STASH):
        os.mkdir(globals.D_STASH)
    if not os.path.exists(os.path.join(globals.D_STASH, 'images')):
        os.mkdir(os.path.join(globals.D_STASH, 'images'))

    if not os.path.exists(globals.D_SRC):
        os.mkdir(globals.D_SRC)
    if not os.path.exists(globals.D_IMG):
        os.mkdir(globals.D_IMG)

def usage():
    print """build-image-commands. Part of the lilyglyphs package.
    Parses a lilyglyphs source file, creates
    single .ly files from it, uses LilyPond to create single glyph
    pdf files and set up template commands to be used in LaTeX.
    For detailed instructions refer to the manual.
    Usage:
    -i filename --input=filename (mandatory): Specifies the input file.

    """




# ####################################
# Finally launch the program
if __name__ == "__main__":
    print 'build-image-commands.py,'
    print 'Part of lilyglyphs.'

    check_paths()

    main(sys.argv[1:])
