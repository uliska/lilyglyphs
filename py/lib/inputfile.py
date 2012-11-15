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
# inputfile.py                                                           #
#                                                                        #
# Handles the definitions input file                                     #
#                                                                        #
# ########################################################################

import os

class InputFile:
    """Handles the input file with command definitions"""
    def __init__(self, file_name):
        # Do file system checks
        if not os.path.exists(file_name):
            raise ValueError('Input file ' + file_name + "doesn't exist")
        elif os.path.isdir(file_name):
            raise ValueError('Input argument ' + file_name + ' is a directory')

        # once we know the file exists we load it to self.lines
        self.file_name = file_name
        self.lines = []
        fin = open(file_name,  'r')
        for line in fin:
            # remove trailing whitespace but not leading (to preserve indentation)
            self.lines.append(line.rstrip())
        fin.close()

    def getLines(self):
        return self.lines


