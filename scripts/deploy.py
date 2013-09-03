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

import os, sys, shutil, zipfile, argparse, datetime

# ################
# Global variables

dir_deploy = 'deploy/lilyglyphs'
manifest = []
    
def main():
    
    if os.path.exists('deploy'):
        overwrite = raw_input('deploy directory exists. Overwrite? ')
        if overwrite != 'y':
            print 'Aborted'
            sys.exit(1)
        shutil.rmtree('deploy')
    os.mkdir('deploy')
    os.mkdir(dir_deploy)
    
    # now we're guaranteed to have an empty 'deploy/lilyglyphs' directory
    
    print 'Copying files:'
    # copy individual files from the root directory
    cp_root()
    # copy complete directories to their corresponding dest
    cp_folder('commands', 'tex/commands')
    cp_folder('core', 'tex/core')
    cp_folder('fonts')
    cp_folder('license')
    cp_folder('source')
    
    # copy lilyglyphs.sty to /tex
    shutil.copy2('lilyglyphs.sty', dir_deploy + '/tex/lilyglyphs.sty')
    manifest.append('/tex/lilyglyphs.sty')
    

    # copy directories to different locations
    cp_folder('glyphimages/definitions', 'source/glyphimages/definitions')
    cp_folder('glyphimages/generated_src', 'source/glyphimages/generated_src')
    cp_folder('glyphimages/pdfs', 'tex/pdfs')
    cp_scripts()
    cp_doc()
    lg_private()
    
    write_manifest()
    write_readme()
    
    # finally pack everything in a zip.
    
    zip = zipfile.ZipFile('deploy/lilyglyphs.zip', 'w')
    os.chdir('deploy')
    for root, dirs, files in os.walk('lilyglyphs/'):
        for file in files:
            zip.write(os.path.join(root, file))
    zip.close()

    
    

def copy_files(f, dst):
    global manifest
    for file in f:
        shutil.copy2(file, dir_deploy + '/' + dst)
        manifest.append(dst + '/' + file)
    
def append_manifest(src, dest):
    for file in os.listdir(src):
        if os.path.isdir(src + '/' + file):
            append_manifest(src + '/' + file, dest + '/' + file)
        manifest.append('/' + dest + '/' + file)

def cp_doc():
    cp_folder('documentation/resources')
    for file in os.listdir('documentation'):
        base, ext = os.path.splitext(file)
        if ext in ['.tex', '.pdf', '.png', '.html']:
            shutil.copy2('documentation/' + file, dir_deploy + '/documentation/' + file)
            manifest.append('/deploy/documentation/' + file)
    os.mkdir(dir_deploy + '/documentation/lilyglyphs_logo')
    for file in os.listdir('documentation/lilyglyphs_logo'):
        base, ext = os.path.splitext(file)
        if ext in ['.tex', '.pdf', '.png']:
            shutil.copy2('documentation/lilyglyphs_logo/' + file, 
                dir_deploy + '/documentation/lilyglyphs_logo/' + file)
            manifest.append('/deploy/documentation/lilyglyphs_logo/' + file)
    
    
def cp_folder(src, dest = None):
    global manifest
    if not dest:
        dest = src
    print '-', src
    shutil.copytree(src, dir_deploy + '/' + dest)
    append_manifest(src, dest)
    
def cp_root():
    print '- root'
    f = []
    f.append('CHANGES.md')
    f.append('INSTALL')
    f.append('README')
    copy_files(f, '')

def cp_scripts():
    print '- scripts'
    os.mkdir(dir_deploy + '/bin')
    os.mkdir(dir_deploy + '/lib')
    for file in os.listdir('scripts'):
        if file.startswith('lily-'):
            shutil.copy2('scripts/' + file, dir_deploy + '/bin')
            manifest.append('/bin/' + file)
        if file.startswith('lilyglyphs') and file.endswith('.py'):
            shutil.copy2('scripts/' + file, dir_deploy + '/lib')
            manifest.append('/lib/' + file)
    
def lg_private():
    print '- lilyglyphs_private'
    zip = zipfile.ZipFile(dir_deploy + '/documentation/lilyglyphs_private.zip', 'w')
    for root, dirs, files in os.walk('lilyglyphs_private'):
        for file in files:
            zip.write(os.path.join(root, file))
    zip.close()
    
def write_readme():
    fout = open(dir_deploy + '/VERSION', 'w')
    fout.write('This is lilyglyphs ' + version + '\n')
    fout.write('Generated on ' + str(datetime.date.today()) + '\n')
    fout.close()
    
    fout = open(dir_deploy + '/tex/README', 'w')
    fout.write('This directory contains files to be found by LaTeX.\n\n')
    fout.write('The core/ and commands/ subdirectories\n')
    fout.write('_must_ remain beside the lilyglyphs.sty package!\n\n')
    fout.write('The pdfs/ subdirectory contains files\n')
    fout.write('that are _used_ by the package.')
    fout.close()
    
def write_manifest():
    global manifest
    fout = open(dir_deploy + '/license/MANIFEST', 'w')
    
    fout.write('MANIFEST for lilyglpyhs ' + version + '\n')
    fout.write('Generated on ' + str(datetime.date.today()) + '\n\n')
    fout.write('The following files are part of this work:\n\n')
    manifest.sort()
    for line in manifest:
        fout.write(line + '\n')
    fout.close()


# ####################################
# Finally launch the program
if __name__ == "__main__":
    
    # parse command line arguments
    parser = argparse.ArgumentParser(
                      description='Prepare lilyglyphs for deployment')
    parser.add_argument('v', 
                        metavar='VERSION', 
                        help='Version to be deployed.')
    args = parser.parse_args()
    version = vars(args)['v']
    version_parts = version.split('.')
    try:
        for part in version_parts:
            int(part)
    except:
        print 'Malformed version argument:', version
        print 'Use three integers separated by dots'
        sys.exit(1)
    
    print 'Preparing lilyglyphs deployment', version + '.'
    print 'CWD is', os.getcwd()
    print 'This should be the root of lilyglyphs.'
    print 'This script will not work on Windows.'
    check = raw_input('Proceed (y/..)? ')
    if check != 'y':
        sys.exit(1)
    
    main()
