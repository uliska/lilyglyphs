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

import os,subprocess

# ################
# Global variables

in_dir = 'generated_src/'
out_dir = 'pdfs/'

def main():

    print 'rebuild-pdfs.py'
    print 'regenerate all pdf images that are not present (anymore)'

    print ''
    print 'Reading file lists, checking missing pdf files'

    # read existing .pdf files in out_dir
    img_files = []
    for file in os.listdir(out_dir):
        name,  ext = os.path.splitext(file)
        if ext == '.pdf':
            img_files.append(name)

    # read existing .ly source files in in_dir
    # and add them to the sources list if the image is missing
    src_files = []
    for file in os.listdir(in_dir):
        name,  ext = os.path.splitext(file)
        if ext == '.ly' and name not in img_files:
            src_files.append(name)

    # is there anything to be done at all?
    if len(src_files) == 0:
        print ''
        print 'No image files missing, nothing to be done.'
        print 'If you want to re-create pdfs, then delete them first'
        return

    print ''
    print 'Found ' + str(len(src_files)) + ' files.'
    print 'Compile with LilyPond:'

    # compile sources
    for file in src_files:
        args = []
        args.append("lilypond")
        args.append("-o")
        args.append(in_dir)
        args.append("-dpreview")
        args.append("-dno-point-and-click")
        args.append(in_dir + file + '.ly')
        subprocess.call(args)
        print ''

        print 'Clean up ' + file
        # remove full-page pdf
        os.remove(in_dir + file + '.pdf')
        # rename/move small 'preview' pdf
        os.rename(in_dir + file + '.preview.pdf',  out_dir + file + '.pdf')

    print 'Remove intermediate files'
    file_list = os.listdir(in_dir)
    for file in file_list:
        dummy, extension = os.path.splitext(file)
        if extension != '.ly':
            os.remove(in_dir + file)


# ####################################
# Finally launch the program
if __name__ == "__main__":
    main()
