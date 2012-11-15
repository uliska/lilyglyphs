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

from commands import Commands
from latexcommand import LatexCommand
from lilyfile import LilypondFile

class GenericCommands(Commands):
    """Responsible for parsing the input file
    """

    def read_entries(self):
        """Parses the input source file and extracts glyph entries"""
        command = ''
        element = ''
        type = 'glyphname'
        comment = []
        def reset_entry():
            command = ''
            element = ''
            type = 'glyphname'
            comment = []
        
        reset_entry()
        print 'Read entries of LilyPond commands:'
        
        for line in self.input_file.getLines():
            line = line.strip()
            # empty line = end of entry
            if not len(line):
                # skip if cmd and glyph haven't been filled both
                if not (command and element):
                    print 'Skip malformed entry \'' + command + '\'. Please check input file'
                    reset_entry()
                # create new Command and set its properties
                else:
                    print 'Read entry \'' + command + '\''
                    cur_cmd = self.newCommand(command)
                    cur_cmd.comment = comment
                    cur_cmd.element = element
                    cur_cmd.type = type
                    cur_cmd.dir = self.cat_subdir
                    if self.scale:
                        cur_cmd.scale = self.scale
                    if self.rais:
                        cur_cmd.rais = self.rais
                    cur_cmd.ltx_cmd = LatexCommand(cur_cmd)
                    reset_entry()
            
            # ignore Python or LaTeX style comments
            elif line[0] in '#%':
                continue
            else:
                key, val = line.split('=')
                key = key.strip()
                if key == 'scale':
                    self.scale = val
                elif key == 'raise':
                    self.rais = val
                elif key == 'comment':
                    comment = [val]
                elif key == 'cmd':
                    command = val
                elif key == 'type':
                    type = val
                elif key == 'element':
                    element = val
        
        
