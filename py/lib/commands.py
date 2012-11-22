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

# This is an internal class, do not try to run it directly
#
# Defines a class representing commands.

import os,  sys,  globals as gl
from command import Command

class Commands:
    """Represents the list of parsed command definitions.
    Should be iterable."""
    def __init__(self):
        self._commands = {}
        self._index = -1
        self._count = 0
        self._scale = ''
        self._raise = ''
        # sorted list of names
        self._names_alpha = []
        # list of names in the order of creation
        self._names_ordered = []

    def add(self, command):
        if not isinstance(command, Command):
            raise TypeError('Not a Command object!')
        cmd_name = command.name
        if cmd_name in self._commands:
            raise ValueError('Command ' + cmd_name + 'already defined')
        else:
            self._commands[cmd_name] = command
            self._names_alpha.append(cmd_name)
            self._names_alpha.sort()
            self._names_ordered.append(cmd_name)

    def __iter__(self):
        return self

    def next(self):
        if self._index == len(self._commands) - 1:
            raise StopIteration
        self._index = self._index + 1
        return self._commands[self._names_alpha[self._index]]

    def byName(self, cmd_name):
        """Returns the command with the given name
        or none if it doesn't exist"""
        result = None
        for cmd in self._commands:
            if cmd.name == cmd_name:
                result = cmd
                break
        return result

    def newCommand(self, cmd_name):
        """Creates and assigns a new Command object
        and returns it"""
        self.commands.append(Command(cmd_name))
        return self.commands[-1]


    def sorted(self):
        """Returns a sorted list of Command instances"""
        names = [cmd.name for cmd in self._commands]
        names.sort()
        return [self.byName(name) for name in names]


