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
    src_files = check_missing_pdfs()
    # is there anything to be done at all?
    if len(src_files) == 0:
        print ''
        print 'No image files missing, nothing to be done.'
        print 'If you want to re-create pdfs, then delete them first'
        sys.exit(0)
    lg.lily_files = src_files
    print ''
    print 'Found ' + str(len(src_files)) + ' missing file(s).'
    
    # compile all LilyPond files without matching pdf
    lg.compile_lily_files()
    
    # clean up directories
    lg.cleanup_lily_files()

def check_missing_pdfs():
    """Compares the list of LilyPond source and resulting PDF files.
       Returns a list of LilyPond source file names (without folder)
       which don't have a corresponding PDF file"""
    print 'Reading file lists, counting missing pdf files'
    img_files = []
    for entry in os.listdir(lg.dir_pdfs):
        entry = os.path.join(lg.dir_pdfs, entry)
        if os.path.isfile(entry):
            path, name =  os.path.split(entry)
            basename,  ext = os.path.splitext(name)
            if ext == '.pdf':
                img_files.append(basename)

    # read existing .ly source files in in_dir
    # and add them to the sources list if the image is missing
    src_files = []
    for entry in os.listdir(lg.dir_lysrc):
        entry = os.path.join(lg.dir_lysrc, entry)
        if os.path.isfile(entry):
            path, name = os.path.split(entry)
            basename,  ext = os.path.splitext(name)
            if ext == '.ly' and basename not in img_files:
                src_files.append(basename)
    return src_files

def check_paths():
    """Checks if we're in the right CWD
       and makes sure that there is a pdf output directory available"""

    print 'Checking directories ...'
    
    # check the presence of the necessary subdirectories
    ls = os.listdir('.')
    if not 'generated_src' in ls:
        print 'No LilyPond source files directory found.'
        print 'Sorry, there is something wrong :-('
        print 'Current working directory is: ' + os.getcwd()
        print 'Please consult the manual.'
        sys.exit(2)
    if not 'pdfs' in ls:
        os.mkdir('pdfs')
    
    print '... done'
    print ''


# ####################################
# Finally launch the program
if __name__ == "__main__":
    main()
