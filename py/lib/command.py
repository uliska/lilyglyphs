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
# command.py                                                             #
#                                                                        #
# defines the class Command                                              #
# which represents the properties of one command.                        #
# The class doesn't implement any functionality                          #
#                                                                        #
# ########################################################################

class Command:
    """Represents a lilyglyphs command.
    Holds input definitions, LilyPond source code and LaTeX commands."""
    def __init__(self, name):
        # command name
        self.name = name
        # comment used for the command
        self.comment = ''
        # content element to be passed to the printing command (in LaTeX)
        self.element = ''
        # type of command, specifies which printing command LaTeX uses
        # and which code template the script uses.
        self.type = ''
        # default scaling that is included in the command definition
        self.scale = ''
        # default raise value for the command definition
        self.rais = ''
        # LilyPond source code (only has content with image driven glyphs)
        self.lilySrc = ''
        # subdirectory for the command
        # (to be used below either the src or the img dir)
        self.dir = ''
        # textual LaTeX representation of the command
        self.ltx_cmd = None
        # LilyPond file representation of the command
        self.lily_cmd = None
