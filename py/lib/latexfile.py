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

import os, textwrap, lilyglyphs_common as lg
import lib.globals as gl
from commands import *
from globals import *


class LatexFile:
    """Writes a LaTeX file with the results of the
    command generation process
    - commands is a Commands instance"""
    def __init__(self, commands):
        self.commands = commands
        self.out_file_name = 'newCommands.tex'
        self.init_templates()

    def write(self):
        """Uses a mixture of internal templates and
        the properties of the Commands objects
        to write a LaTeX file to disk."""
        fout = open(os.path.join(gl.d_stash, self.out_file_name), 'w')
        fout.write('% New Glyphs for the lilyglyphs package\n')
        fout.write(lg.signature() + '\n')
        fout.write(self.start_comment.replace('SCRIPT_NAME', lg.script_name()))

        # retrieve a sorted list of LatexCommand instances
        cmd_objs = []
        for cmd in self.commands.sorted():
            cmd_objs.append(cmd.ltx_cmd)

        # write out command definitions
        for cmd in cmd_objs:
            fout.write(cmd.comment)
            fout.write(cmd.command)

        # write out \begin{document} and heading
        fout.write(self.begin_document)
        fout.write(lg.signature()[2:]+ '\n')

        # write out reference table
        row_template = '\\CMD & \\cmd{CMD} & description\\\\' + '\n'
        reftable_content = ''
        for cmd in cmd_objs:
            reftable_content += '    ' + row_template.replace('CMD', cmd.name)
        fout.write(self.tmpl_reftable.replace('REFTABLE', reftable_content))

        # write out test code for each command
        fout.write(self.testcode_start)
        for cmd in cmd_objs:
            fout.write(cmd.testcode)

        # finish document
        fout.write('\\end{document}\n')
        fout.close()


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




