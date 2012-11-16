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
        self.root_dir = root_dir
        self.full_name = os.path.join(root_dir, rel_file)
        self.rel_dir, self.file_name = os.path.split(rel_file)
        self.full_dir = os.path.join(root_dir, self.rel_dir)
        self.name, self.ext = os.path.splitext(self.file_name)
        self.full_basename = os.path.join(self.full_dir, self.name)
        self.rel_basename = os.path.join(self.rel_dir, self.name)
        
        
        
        
