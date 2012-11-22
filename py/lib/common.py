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
# common.py                                                              #
#                                                                        #
# Common functionality for the Python scripts in lilyglyphs              #
#                                                                        #
# ########################################################################

import os, sys, datetime, globals as gl

def check_duplicates(files):
    """Checks for file entries that occur more than once.
    Checks for the 'count' member.
    If there are duplicates they are printed to the console,
    then program terminates"""
    dups_list = []
    for file in files:
        if files[file]['count'] > 1:
            dups_list.append(file + files[file]['ext'])
    if dups_list:
        print ''
        print 'The following files exist in more than one'
        print 'subdirectory of ' + os.path.join(os.getcwd(), dir_lysrc) + ','
        print 'please check:'
        for entry in dups_list:
            print entry + '\n'
        sys.exit('Abort')


def check_lilyglyphs_root(subdir = ''):
    """Checks if the current working directory
       is within the rootline of the lilyglyphs package.
       If this is the case it sets the cwd to be
       the root of the package or the subdir
       given as the argument."""

    print 'Checking directories'

    # check current working dir
    cwd = os.getcwd()
    if not 'lilyglyphs' in cwd:
        print 'Your current working directory seems to be wrong.'
        print 'Please cd to a location in the lilyglyphs directory.'
        sys.exit(2)

    # set global variable
    gl.LILYGLYPHS_ROOT = cwd[:cwd.find('lilyglyphs') + 10]
    gl.D_STASH = os.path.join(gl.LILYGLYPHS_ROOT, gl.D_STASH_ROOT)
    # set current working dir
    os.chdir(gl.LILYGLYPHS_ROOT)
    # if there is a subdir as argument,
    # then change there (subdir must exist)
    if subdir:
        os.chdir(subdir)


def cleanup_lily_files():
    """Removes unneccessary files from LilyPond compilation,
    rename and remove the preview PDF files to the right directory."""

    print 'Clean up directories'

    # iterate through the subdirectories of dir_lysrc
    for entry in os.listdir(gl.D_SRC):
        in_dir = os.path.join(gl.D_SRC, entry)
        if os.path.isdir(in_dir):
            # make sure there is a corresponding dir_pdfs directory
            out_dir = os.path.join(gl.D_IMG, entry)
            if not os.path.exists(out_dir):
                os.mkdir(out_dir)
            # iterate through the subdir
            for file in os.listdir(in_dir):
                name, extension = os.path.splitext(file)
                #remove unnecessary files
                if not extension in ['.pdf', '.ly']:
                    os.remove(os.path.join(in_dir, file))
                if extension == '.pdf':
                    # remove full-page pdf
                    if not '.preview' in name:
                        os.remove(os.path.join(in_dir, file))
                    else:
                        newfile = file.replace('.preview.', '.')
                        # rename/move small 'preview' pdf
                        os.rename(os.path.join(in_dir, file),  os.path.join(out_dir, newfile))


# This is deprecated and shouldn't work anymore
def compare_file_lists(list_in, list_out):
    """Compares two filelist dictionaries.
    The key for the dictionaries is the command name.
    The value is another dictionary that has to contain 'dir' and 'ext' keys
    Returns a list with the full names of all files
    present in list_out but not in list_in"""
    diff = []
    for file in list_in:
        if file not in list_out:
            diff.append(os.path.join(list_in[file]['dir'], file + list_in[file]['ext']))
    return diff



def list_files(basedir):
    """Returns a dictionary of all files in basedir and its subdirectories"""
    files = {}
    for entry in os.listdir(basedir):
        if basedir[-1] == '/':
            basedir = basedir[:-1]
        if os.path.isdir(basedir + '/' + entry):
            new_files = list_files(basedir + '/' + entry)
            for file in new_files:
                if file in files:
                    files[file]['count'] = files[file]['count'] + 1
                else:
                    files[file] = new_files[file]
        else:
            name, ext = os.path.splitext(entry)
            files[name] = {}
            files[name]['dir'] = basedir
            files[name]['ext'] = ext
            files[name]['count'] = 1
    return files

def script_name():
    """Returns the name of the current script.
    Used in comments in the generated files"""
    dummy, result = os.path.split(sys.argv[0])
    return result

def signature():
    """Returns a signature to be inserted in an output file"""
    return '% created by ' + script_name() + ' on ' + str(datetime.date.today())


