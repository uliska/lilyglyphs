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
# lilyglyphs_file_tree.py                                                #
#                                                                        #
# A file tree for the lilyglyphs package                                 #
# Represents either a source or an image file tree                       #
#                                                                        #
# ########################################################################

import os
from lilyglyphs_file import LilyglyphsFile

class LilyglyphsFileTree:
    def __init__(self, root):
        if not os.path.exists(root):
            raise OSError('Root directory ' + root + ' does not exist')
        self.root_dir = root
        self.dirs = []
        self.files = []
        self.__read_tree('')


    def check_duplicates(self):
        """Returns True (and prints a message)
           if there are duplicates present.
           Returns False if no duplicates exist"""
        if self.has_duplicates():
            print 'There are duplicate entries in the file tree\n     ',
            print self.root_dir
            print 'Please check manually and remove or rename the duplicates'
            print '(because they represent duplicate command definitions).'
            print self.get_duplicates()
        return self.has_duplicates()

    def check_stale_files(self, other_tree):
        """Returns True (and prints a message)
           if there are files in the tree that
           are not present in the given other tree.
           Returns False if no stale files are found.

           other_tree is an instance of LilyglyphsFileTree"""
        stale_files = self.get_files_not_in_tree(other_tree)
        if stale_files:
            print 'There are files in the file tree\n     ',
            print self.root_dir
            print 'that are not present in the tree\     ',
            print other_tree.root_dir
            print 'You may want to check if you have to remove them manually:'
            print stale_files
            return True
        else:
            return False

    def get_duplicates(self):
        result = {}
        names = {}
        for file in self.files:
            if file.name in names :
                if file.name in result:
                    result[file.name].append(file.full_name)
                else:
                    result[file.name] = [names[file.name], file.full_name]
            else:
                names[file.name] = file.full_name
        return result

    def get_files_not_in_tree(self, other_tree):
        own_files = self.get_rel_basenames()
        other_files = other_tree.get_rel_basenames()
        return [file for file in own_files if file not in other_files]

    def get_full_basenames(self):
        return [file.full_basename for file in self.files]

    def get_full_filenames(self):
        return [file.full_name for file in self.files]

    def get_rel_basenames(self):
        return [file.rel_basename for file in self.files]

    def __read_tree(self, rel_dir):
        """Returns a dictionary of all files in rel_dir and its subdirectories
        rel_dirs are relative to the filetree root,
        full_dirs are relative to the CWD"""
        full_dir = os.path.join(self.root_dir, rel_dir)

        for entry in sorted(os.listdir(full_dir)):
            full_entry = os.path.join(full_dir, entry)
            if os.path.isdir(full_entry):
                self.dirs.append(full_entry)
                self.__read_tree(os.path.join(rel_dir, entry))
            else:
                if not entry[0] == '.':
                    self.files.append(LilyglyphsFile(self.root_dir, os.path.join(rel_dir, entry)))


class LilyglyphsSrcFileTree(LilyglyphsFileTree):
    pass
