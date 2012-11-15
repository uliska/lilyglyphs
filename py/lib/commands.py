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

# This is an internal class, do not try to run it directly
#
# Defines a class representing commands.

import os,  sys,  globals as gl
from latexcommand import LatexCommand
from command import Command
from inputfile import InputFile

class Commands:
    """Represents the list of parsed command definitions.
    Should be iterable."""
    def __init__(self, file_name):
        self.commands = []
        self.index = -1
        self.count = 0
        self.scale = ''
        self.rais = ''
        self.set_input_file(file_name)

    def __iter__(self):
        return self

    def next(self):
        if self.index == len(self.commands) - 1:
            raise StopIteration
        self.index = self.index + 1
        return self.commands[self.index]

    def byName(self, cmd_name):
        """Returns the command with the given name
        or none if it doesn't exist"""
        result = None
        for cmd in self.commands:
            if cmd.name == cmd_name:
                result = cmd
                break
        return result

    def newCommand(self, cmd_name):
        """Creates and assigns a new Command object
        and returns it"""
        self.commands.append(Command(cmd_name))
        return self.commands[-1]

    def read_entries(self):
        """Has to be overridden by inheriting classes
        This function is responsible for creating
        individual Command instances, populating them
        with its properties, and also to create
        a LatexCommand instance for the Command"""
        pass

    def set_input_file(self, file_name):
        """Tries to open the given input file.
        If that works it reads the entries from the file
        (and thus builds the list of Command instances)"""
        try:
            inp_file_name = os.path.join(gl.d_defs, file_name)
            self.input_file = InputFile(inp_file_name)
        except ValueError:
            print 'Input file ' + file_name + ' not found.'
            sys.exit('Abort')

        # the 'category subdir' will be used for writing lilypond and pdf files
        # basename of input file is also used for this purpose
        self.cat_subdir, dummy = os.path.splitext(file_name)

        # reset commands
        self.commands = []
        self.rais = gl.DEF_RAISE
        self.scale = gl.DEF_SCALE

        # read_entries() has to
        self.read_entries()

        # set counter for the iterator
        self.count = len(self.commands)

    def sorted(self):
        """Returns a sorted list of Command instances"""
        names = [cmd.name for cmd in self.commands]
        names.sort()
        return [self.byName(name) for name in names]


