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
# inputfile.py                                                           #
#                                                                        #
# Handles the definitions input file                                     #
#                                                                        #
# ########################################################################

import os, globals as gl, common as lg
from lilyglyphs_file import LilyglyphsFile
from commands import Commands
from latexfile import LatexFile

class InputFile(LilyglyphsFile):
    """Handles an input file with command definitions"""
    def __init__(self, file_name):
        """Create an instance.

           file_name is relative to lg.D_DEFS"""

        # Call superclass intializer
        LilyglyphsFile.__init__(self, gl.D_DEFS,  file_name)

        # create empty Commands object
        self._commands = Commands()

        # Do file system checks
        if not os.path.exists(self._full_name):
            raise ValueError('Input file ' + self._full_name + "doesn't exist")
        elif os.path.isdir(self._full_name):
            raise ValueError('Input argument ' + self._full_name + ' is a directory')

        # once we know the file exists we load it to self.lines
        self._load()

        # reset the default values for the optional argument
        self.rais = gl.DEF_RAISE
        self.scale = gl.DEF_SCALE

        # parse the file and generate the Commands entries
        self._read_entries()

        # generate the LaTeX file from my own content
        ltx_cmds = []
        for cmd in self._commands:
            ltx_cmds.append(cmd.latex_cmd)
        ltx_out_name = os.path.join(gl.D_STASH, self._rel_basename + '.tex')
        self._latex_file = LatexFile(ltx_cmds, ltx_out_name)

        # finally write myself out to disk
        self._latex_file.write()

    def get_lines(self):
        return self._lines

    def _load(self):
        fin = open(self._full_name,  'r')
        for line in fin:
            # remove trailing whitespace but not leading (to preserve indentation)
            self._lines.append(line.rstrip())
        fin.close()

    def _read_entries(self):
        """Has to be overridden by inheriting classes
        This function is responsible for creating
        individual Command instances, populating them
        with its properties, and also to create
        a LatexCommand instance for the Command"""
        pass
        # TODO: raise an appropriate Exception



