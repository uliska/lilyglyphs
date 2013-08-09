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
# deploy.py                                                              #
#                                                                        #
# copies all needed files to the deployable archive                      #
#                                                                        #
# ATTENTION:                                                             #
# Before using this script, please check if it is still up to date       #
# (i.e. if the files to be deployed are still correct and present)       #
#                                                                        #
# ########################################################################

import lilyglyphs_common as lg, os, sys, tarfile, shutil

# ################
# Global variables

dir_deploy = 'deploy/'
tar = None

def main():
    global tar,  version
    lg.check_lilyglyphs_root()
    if not os.path.exists(dir_deploy):
        os.mkdir(dir_deploy)
    archive_name = dir_deploy + 'lilyglyphs-' + version + '.tar.gz'
    tar = tarfile.open(archive_name, 'w:gz')

    print 'Add files to ' + archive_name
    add_root()
    add_documentation()
    add_glyphimages()
    tar.close()
    
    tar = tarfile.open('deploy/lilyglyphs-fonts.tar.gz', 'w:gz')
    tar.add('otf')
    tar.close()
    
def add_documentation():
    global tar,  version
    f = []
    tar.add('documentation/lilyglyphs.pdf', 'lilyglyphs-' + version + '.pdf')
    shutil.copy2('documentation/lilyglyphs.pdf', 'deploy/lilyglyphs-' + version + '.pdf')
    
    
def add_files(files,  dir):
    global tar
    for file in files:
        if not os.path.exists(file):
            print 'Missing from ' + dir + ': ' + file
        else:
            tar.add(file)
    
def add_glyphimages():
    f = []
    f.append('glyphimages/pdfs')
    logo_base = 'glyphimages/lilyglyphs_logo/lilyglyphs_logo.'
    f.append(logo_base + 'pdf')
    f.append(logo_base + 'png')
    add_files(f, 'glyphimages')
    
def add_root():
    f = []
    f.append('CHANGES.md')
    f.append('COPYING')
    f.append('INSTALL.md')
    f.append('README.md')
    f.append('lilyglyphs.sty')
    f.append('lilyglyphsStyle.sty')
    f.append('commands')
    f.append('core')
    f.append('glyphlist')
    add_files(f, 'root')
    
    
# ####################################
# Finally launch the program
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'No version number argument given.\n'
        sys.exit(2)
    version = str(sys.argv[1])
    main()
