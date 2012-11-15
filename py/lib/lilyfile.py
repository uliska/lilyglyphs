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
# imagecommands.py                                                       #
#                                                                        #
# defines the class ImageCommands(Commands)                              #
# which extends Commands                                                 #
# and is responsible for parsing the input file for image driven commands#
#                                                                        #
# ########################################################################

import os, subprocess, common as lg, globals as gl
from strings import *

class LilypondFile:
    def __init__(self, command = None):
        self.has_command = False
        if command:
            self.has_command = True
            self.lines = []
            self.command = command
            self.dir = command.dir
            self.full_dir = os.path.join(gl.d_src, self.dir)
            self.file_name = os.path.join(self.full_dir, command.name + '.ly')
            self.generate()

    def compile(self):
        """Compiles LilyPond files"""
        print 'Compile with LilyPond:'
        args = []
        args.append('lilypond')
        args.append('-o')
        args.append(os.path.join(gl.d_src, self.dir))
        args.append('-dpreview')
        args.append('-dno-point-and-click')
        args.append(self.file_name)
        subprocess.call(args)
        print ''

    def generate(self):
        if not self.has_command:
            raise ValueError('Cannot call generate() on a LilypondFile without lilySrc')

        self.lines = []

        #output the license information
        self.lines.append(lilyglyphs_copyright_string)
        self.lines.append('')

        #output information on the actual file
        self.__file_info()

        #write the default LilyPond stuff
        self.lines.append(lily_src_prefix)

        # write the comment for the command
        self.lines.append('%{\n')
        for line in self.command.comment:
            self.lines.append('  ' + line + '\n')
        self.lines.append('%}\n\n')

        # write the actual command
        self.lines.append(self.command.name + ' = {\n')
        for line in self.command.lilySrc:
            self.lines.append(line + '\n')
        self.lines.append('}\n')

        # write the score definition
        self.lines.append(lily_src_score)

        # finish the LilyPond file
        self.lines.append('  \\' + self.command.name + '\n')
        self.lines.append('}\n\n')




    def __file_info(self):
        """Formats file specific information for the lilyPond source file"""
        long_line = '% This file defines a single glyph to be created with LilyPond: %\n'
        width = len(long_line) - 1
        header = '%' * width + '\n'
        spacer = '%' + ' ' * (width - 2) + '%\n'
        padding = width - len(self.command.name) - 8
        self.lines.append(header)
        self.lines.append(spacer)
        self.lines.append(long_line)
        self.lines.append(spacer)
        self.lines.append('%   ' + self.command.name + '.ly' + ' ' * padding + '%\n')
        self.lines.append(spacer)
        self.lines.append(header)
        self.lines.append(lg.signature())
        self.lines.append('\n\n')

    def write(self):
        if not self.has_command:
            raise ValueError('Cannot call write() on a LilypondFile without lilySrc')
        if not os.path.exists(self.full_dir):
            os.mkdir(self.full_dir)
        print '- ' + self.command.name
        # open a single lily src file for write access
        fout = open(self.file_name, 'w')
        for line in self.lines:
            fout.write(line)
        fout.close()



