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

class LilyglyphsFile:
    def __init__(self, root_dir, rel_file):
        # root dir of the file tree this file belongs to
        # (relative to CWD)
        self._root_dir = root_dir
        # full name of the file, relative to CWD
        self._full_name = os.path.join(root_dir, rel_file)
        # file name relative to root_dir (i.e. the current file tree)
        # (used to compare different trees
        self._rel_name = rel_file
        # diretory the file is in, relative to the file tree
        # plain file name (with extension)
        self._rel_dir, self._file_name = os.path.split(rel_file)
        # directory the file is in, relative to CWD
        self._full_dir = os.path.join(root_dir, self._rel_dir)
        # base name of the file (corresponding e.g. to a command name)
        # file extension,
        # may be used to determine if the file shold be included in a collection
        #self._name = ''
        #self._ext = ''
        self._name, self._ext = os.path.splitext(self._file_name)
        # full basename, without extension, with path
        # (relative to CWD)
        self._full_basename = os.path.join(self._full_dir, self._name)
        # basename, without extension, with path
        # (relative to the file tree)
        self._rel_basename = os.path.join(self._rel_dir, self._name)
        # string list, containing the plain contents of the file
        self._lines = []

    def get_ext(self):
        return self._ext

    def get_file_name(self):
        return self._file_name

    def get_full_basename(self):
        return self._full_basename

    def get_full_dir(self):
        return self._full_dir

    def get_full_name(self):
        return self._full_name

    def get_name(self):
        return self._name

    def get_rel_basename(self):
        return self._rel_basename

    def get_rel_name(self):
        return self._rel_name

    def get_rel_dir(self):
        return self._rel_dir

    def get_root_dir(self):
        return self._root_dir


    def write(self):
        """Writes out the content of the file to disk.
           Any existing file will be overwritten!"""
        fout = open(self._full_name, 'w')
        for line in self._lines:
            fout.write(line + '\n')
        fout.close()



