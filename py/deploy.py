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
    add_files(f, gl.GLYPH_IMG_ROOT)
    
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
