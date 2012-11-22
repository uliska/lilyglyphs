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
# imagecommands.py                                                       #
#                                                                        #
# defines the class ImageCommands(Commands)                              #
# which extends Commands                                                 #
# and is responsible for parsing the input file for image driven commands#
#                                                                        #
# ########################################################################

from command import Command
from commands import Commands
from inputfile import InputFile
from latexcommand import LatexCommand

class InputFileGeneric(InputFile):
    """Responsible for parsing the input file
    of the generic commands definitions file"""

    def _read_entries(self):
        """Parses the input source file and extracts glyph entries"""
        command = ''
        element = ''
        type = 'glyphname'
        comment = []

        print 'Read entries of LilyPond commands:'

        for line in self._lines:
            line = line.strip()
            # empty line = end of entry
            if not len(line):
                # skip if cmd and glyph haven't been filled both
                if not (command and element):
                    print 'Skip malformed entry \'' + command + '\'. Please check input file'
                    command = ''
                    element = ''
                    type = 'glyphname'
                    comment = []

                # create new Command and set its properties
                else:
                    print 'Read entry \'' + command + '\''
                    cur_cmd = Command(command)
                    cur_cmd.set_comment(comment)
                    cur_cmd.set_element(element)
                    cur_cmd.set_type(type)
                    if self.scale:
                        cur_cmd.scale = self.scale
                    if self._raise:
                        cur_cmd.set_raise(self._raise)
                    cur_cmd.set_latex_cmd(LatexCommand(cur_cmd))
                    self._commands.add(cur_cmd)

                    # reset properties
                    cur_cmd = None
                    command = ''
                    element = ''
                    type = 'glyphname'
                    comment = []

            # ignore Python or LaTeX style comments
            elif line[0] in '#%':
                continue
            else:
                key, val = line.split('=')
                key = key.strip()

                if key == 'scale':
                        self._scale = val
                elif key == 'raise':
                    self._raise = val
                elif key == 'comment':
                    comment = [val]
                elif key == 'cmd':
                    command = val
                elif key == 'type':
                    type = val
                elif key == 'element':
                    element = val


