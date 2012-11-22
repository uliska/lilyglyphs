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
# latexfile.py                                                           #
#                                                                        #
# defines the LatexFile class,                                           #
# that only writes out a LaTeX result file                               #
#                                                                        #
# ########################################################################

import os, textwrap, common as lg
from commands import Commands
from globals import *
from lilyglyphs_file import LilyglyphsFile
from latexcommand import LatexCommand


class LatexFile(LilyglyphsFile):
    """Writes a LaTeX file with the results of the
    command generation process
    - commands is a Commands instance"""
    def __init__(self, commands, filename):


        LilyglyphsFile.__init__(self, D_STASH,  filename)
        for cmd in commands:
            if not isinstance(cmd, LatexCommand):
                raise TypeError('Not a LatexCommand instance')
        self._commands = commands

        self.init_templates()
        self.generate()

    def generate(self):
        """Generates the textual representation of the
           LaTeX file from the commands object
           Uses a mixture of internal templates and
           the properties of the Commands objects"""

        self._lines.append('% New Glyphs for the lilyglyphs package\n')
        self._lines.append(lg.signature() + '\n')
        self._lines.append(self.start_comment.replace('SCRIPT_NAME', lg.script_name()))

        # write out command definitions
        for cmd in self._commands:
            self._lines.append(cmd.comment)
            self._lines.append(cmd.command)

        # write out \begin{document} and heading
        self._lines.append(self.begin_document)
        self._lines.append(lg.signature()[2:]+ '\n')

        # write out reference table
        row_template = '\\CMD & \\cmd{CMD} & description\\\\' + '\n'
        reftable_content = ''
        for cmd in self._commands:
            reftable_content += '    ' + row_template.replace('CMD', cmd.name)
        self._lines.append(self.tmpl_reftable.replace('REFTABLE', reftable_content))

        # write out test code for each command
        self._lines.append(self.testcode_start)
        for cmd in self._commands:
            self._lines.append(cmd.testcode)

        # finish document
        self._lines.append('\\end{document}\n')


    def init_templates(self):
        self.begin_document = textwrap.dedent("""\

            \\begin{document}

            %%%%%%%%%%%%%
            % Text output

            \\section*{New \\lilyglyphs{} commands}
            """)

        self.tmpl_reftable = textwrap.dedent("""\

            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            % Reference table to be used in the manual
            % (use complete or single lines)

            \\begin{reftable}{New commands}{newcommands}
            REFTABLE\\end{reftable}
            """)

        self.start_comment = textwrap.dedent("""\
            %
            % This file contains definitions for the new commands
            % along with test code for them.
            % You can test the commands in the context of continuous text
            % and adjust their design time options.
            % Afterwards you should manually move the commands to
            % the appropriate .inp files,
            % because this file will be overwritten by the next run
            % of SCRIPT_NAME!
            % If you want to keep this file for reference
            % you should save it with a new name.
            %
            % There also is a table containing entries for use in the lilyglyph manual.
            % You can either copy the whole table to the appropriate
            % place in lilyglyphs.tex or just copy individual table rows.

            \\documentclass{scrartcl}
            \\usepackage{lilyglyphsStyle}

            %%%%%%%%%%%%%%%%%%%%%%%%%
            % new command definitions

            """)

        self.testcode_start = textwrap.dedent("""\

            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            % Test code for fine-tuning the new commands

            """)




