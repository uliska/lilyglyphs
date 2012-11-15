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

import lilyglyphs_common as lg, os, sys, subprocess

# ################
# Global variables

def main():

    print 'rebuild-pdfs.py'
    print 'regenerate all pdf images that are not present (anymore)'
    
    print ''
    check_paths()
    
    print ''
    print 'Listing generated LilyPond source files'
    src_files = lg.list_files(lg.dir_lysrc)
    lg.check_duplicates(src_files)
    
    print ''
    print 'Listing generated PDF files'
    img_files = lg.list_files(lg.dir_pdfs)
    lg.check_duplicates(img_files)
    
    print ''
    print 'Comparing lists'
    missing_pdfs = lg.compare_file_lists(src_files, img_files)

    if not missing_pdfs:
        print ''
        print 'No image files missing, nothing to be done.'
        print 'If you want to re-create pdfs, then delete them first'
        sys.exit(0)
    
    print ''
    print 'Found missing pdf files and will re-create them with LilyPond:'
    for file in missing_pdfs:
        print file
    
    lg.compile_src_files(missing_pdfs)
    
    lg.cleanup_lily_files()


def check_paths():
    """Sets CWD to 'glyphimages' subdir
       and makes sure that the necessary subdirectories are present"""
    global lilyglyphs_root
    lg.check_lilyglyphs_root()
    os.chdir('glyphimages')

    # check the presence of the necessary subdirectories
    ls = os.listdir('.')
    if not 'generated_src' in ls:
        print 'No LilyPond source files directory found.'
        print 'Sorry, there is something wrong :-('
        sys.exit(2)
    if not 'pdfs' in ls:
        os.mkdir('pdfs')
    

# ####################################
# Finally launch the program
if __name__ == "__main__":
    main()
