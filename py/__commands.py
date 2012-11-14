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

import os,  sys


d_defs = 'definitions'
d_src = 'generated_src'
d_img = 'generated_img'
d_stash = 'stash_new_commands'

scale = ''
rais = ''


class Command:
    """Represents a lilyglyphs command.
    Holds input definitions, LilyPond commands and LaTeX commands."""
    def __init__(self, name):
        self.name = name
        self.comment = ''
        self.lilySrc = ''
        self.element = ''
        self.type = ''
        self.dir = ''
        self.scale = ''
        self.rais = ''
        self.ltx_cmd = ''
        self.ltx_testcode = ''


class InputFile:
    """Handles the input file with command definitions"""
    def __init__(self, file_name):
        if not os.path.exists(file_name):
            raise ValueError('Input file ' + file_name + "doesn't exist")
        self.__lines = []
        self.file_name = file_name
        self.load_from_file()

    def getLines(self):
        return self.__lines

    def load_from_file(self):
        """Loads the content of the file into the stringlist lines"""
        fin = open(self.file_name,  'r')
        for line in fin:
            self.__lines.append(line.rstrip())
        fin.close()


class Commands:
    def __init__(self, file_name):
        self.commands = []
        self.index = -1
        self.count = 0
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
            if cmd.Name == cmd_name:
                result = cmd
                break
        return result

    def newCommand(self, cmd_name):
        self.commands.append(Command(cmd_name))
        return self.commands[-1]

    def read_entries(self):
        pass
    def read_entry(self):
        pass

    def set_input_file(self, file_name):
        try:
            inp_file_name = os.path.join(d_defs, file_name)
            self.input_file = InputFile(inp_file_name)
        except ValueError:
            print 'Input file ' + file_name + ' not found.'
            sys.exit('Abort')

        # the 'category subdir' will be used for writing lilypond and pdf files
        # basename of input file is also used for this purpose
        self.cat_subdir, dummy = os.path.splitext(file_name)
        self.read_entries()

        # set counter for the iterator
        self.count = len(self.commands)


class ImageCommands(Commands):

    def read_entries(self):
        """Parses the input source file and extracts glyph entries"""
        print 'Read entries of LilyPond commands:'
        lines = self.input_file.getLines()
        for i in range(len(lines)):
            if '%%lilyglyphs' in lines[i]:
                i = self.read_entry(i)

    def read_entry(self, i):
        """Reads a single glyph entry from the input file and stores it
        in the global dictionary lg.in_cmds"""
        global scale,  rais

        lines = self.input_file.getLines()
        # read comment line(s)
        i += 1
        is_protected = False
        comment = []
        # loop over the comment line(s)
        while i < len(lines):
            line = lines[i].strip()
            if not line[0] == '%':
                break
            # check for 'protected' entries that shouldn't be processed newly
            elif '%%protected' in line:
                is_protected = True
            # check for scale or raise arguments that set new default values
            elif 'scale=' in line:
                dummy, scale = line.split('=')
            elif 'raise=' in line:
                dummy,  rais = line.split('=')
            else:
                line = line[1:].strip()
                comment.append(line)
            i += 1

        # skip any empty lines between comment and definition
        while len(lines[i].strip()) == 0:
            i += 1

        # read command name
        line = lines[i].strip()
        name,  dummy = line.split('=')
        name = name.strip()

        print '- ' + name,
        if is_protected:
            print ' (protected and skipped)'
        else:
            print '' #(for line break only)

        # read actual command until we find a line the begins with a closing curly bracket
        i += 1
        lilySrc = []
        while lines[i][0] != '}':
            lilySrc.append(lines[i])
            i += 1
        if not is_protected:
            cur_cmd = self.newCommand(name)
            cur_cmd.comment = comment
            cur_cmd.lilySrc = lilySrc
            cur_cmd.element = name
            cur_cmd.type = 'image'
            cur_cmd.dir = self.cat_subdir
            if scale:
                cur_cmd.scale = scale
            if rais:
                cur_cmd.rais = rais

        return i


