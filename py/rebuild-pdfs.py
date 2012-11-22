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

# ########################################################################
#                                                                        #
#   rebuild-pdfs.py                                                      #
#                                                                        #
# This program looks in the directories where the generated .ly files    #
# and the generated pdf images are stored.                               #
# If it finds that there are missing pdfs it will recompile them         #
# using LilyPond.                                                        #
#                                                                        #
# The main purpose is to allow the creation of pdf images of glyphs      #
# that have been marked 'protected' in the input definitions,            #
# but that aren't present because they aren't tracked by Git             #
#                                                                        #
# ########################################################################

import lib.common as lg, lib.globals as gl
import os, sys, subprocess
from lib.lilyfile import LilypondFile
from lib.lilyglyphs_file_tree import LilyglyphsFileTree


# ################
# Global variables

def main():

    print 'Reading generated LilyPond source file tree'
    src_file_tree = LilyglyphsSrcFileTree(gl.D_SRC)
    # consistency check for duplicate entries in the source tree
    if src_file_tree.check_duplicates():
        sys.exit('Operation aborted')

    print 'Reading generated image file tree'
    img_file_tree = LilyglyphsFileTree(gl.D_IMG)
    # check for 'stale' files, i.e. destination files not present in the
    # source file directory.
    # Such stale files should only exist after source files have been
    # (re-)moved, so they should be pruned.
    if img_file_tree.check_stale_files():
        print '(Operation is continued anyway)'


    # check for source files that don't have a corresponding pdf file
    # in the output directory. These are the ones we want to regenerate
    missing_img_files = src_file_tree.get_files_not_in_tree(img_file_tree)
    if missing_img_files:
        print 'The following pdf files are missing'
        print 'and will be re-generated with LilyPond:'
        print missing_img_files
    else:
        print 'No image files missing, nothing to be done.'
        print 'If you want to re-create pdfs, then delete them first'
        sys.exit(0)

    for file in missing_img_files:
        file.compile()

    lg.cleanup_lily_files()


def check_paths():
    """Sets CWD to gl.GLYPH_IMG_ROOT subdir
       and makes sure that the necessary subdirectories are present"""
    lg.check_lilyglyphs_root(gl.GLYPH_IMG_ROOT)

    # check the presence of the necessary subdirectories
    ls = os.listdir('.')
    # If the source directory isn't present
    # something has to be fundamentally wrong (can only abort)
    if not gl.D_SRC in ls:
        print 'No LilyPond source files directory found.'
        print 'Sorry, there is something wrong :-('
        print 'Current working directory is:', os.getcwd()
        print 'Source directory should be:', gl.D_SRC
        sys.exit(2)
    # If the image directory isn't present,
    # we'll create it empty
    if not gl.D_IMG in ls:
        os.mkdir(gl.D_IMG)
    print ''



# ####################################
# Finally launch the program
if __name__ == "__main__":
    print 'rebuild-pdfs.py'
    print '(Re-)generate all pdf images that are not present (anymore)'
    print ''
    check_paths()
    main()
