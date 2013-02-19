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
# inputfileimages.py                                                     #
#                                                                        #
# defines the class ImputFileImages(InputFile)                           #
# which extends InputFile                                                #
# and is responsible for parsing the input file for image driven commands#
#                                                                        #
# ########################################################################

from inputfile import InputFile
from latexcommand import LatexCommand
from lilypondfile import LilypondFile
from command import Command

class InputFileImages(InputFile):
    """Responsible for parsing the input file
    for image driven commands"""

    def compile_lily_files(self):
        for cmd in self.commands:
            cmd.lily_cmd.compile()

    def read_entries(self):
        """Parses the input source file and extracts glyph entries"""
        print 'Read entries of LilyPond commands:'
        InputFile.read_entries(self)
        for i in range(len(self._lines)):
            if '%%lilyglyphs' in self._lines[i]:
                i = self.read_entry(i)

    def read_entry(self, i):
        """Reads a single glyph entry from the input file and stores it
        in the global dictionary lg.in_cmds"""

        # read comment line(s)
        i += 1
        is_protected = False
        comment = []
        # loop over the comment line(s)
        while i < len(self._lines):
            line = self._lines[i].strip()
            if not line[0] == '%':
                break
            # check for 'protected' entries that shouldn't be processed newly
            elif '%%protected' in line:
                is_protected = True
            # check for scale or raise arguments that set new default values
            elif 'scale=' in line:
                dummy, self.scale = line.split('=')
            elif 'raise=' in line:
                dummy, self.rais = line.split('=')
            else:
                line = line[1:].strip()
                comment.append(line)
            i += 1

        # skip any empty lines between comment and definition
        while len(self._lines[i].strip()) == 0:
            i += 1

        # read command name
        line = self._lines[i].strip()
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
        while self._lines[i][0] != '}':
            lilySrc.append(self._lines[i])
            i += 1

        # if the entry isn't marked as protected
        # create a new Command and generate
        # LatexCommand and LilypondFile from it.
        if not is_protected:
            cur_cmd = Command(name)
            cur_cmd.dir = self._rel_basename
            cur_cmd.set_comment(comment)

            cur_cmd.lilySrc = lilySrc

            cur_cmd.set_element(name)


            cur_cmd.set_type('image')

            if self._scale:
                cur_cmd._scale = self._scale
            if self._raise:
                cur_cmd._raise = self._raise

            self._commands.add(cur_cmd)
            cur_cmd.set_latex_cmd(LatexCommand(cur_cmd))

            cur_cmd.lily_cmd = LilypondFile(self, cur_cmd)


            # reset properties
            cur_cmd = None
            command = ''
            element = ''
            comment = []


        return i

    def write_lily_src_files(self):
        """Iterates over the commands
        and lets each one write out its Lilypond source file"""
        for cmd in self.commands:
            cmd.lily_cmd.write()

