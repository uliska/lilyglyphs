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
# latexcommand.py                                                        #
#                                                                        #
# defines the class LatexCommand                                         #
# that represents the processed parts of the LaTeX command               #
#                                                                        #
# ########################################################################

import textwrap, common as lg, globals as gl

class LatexCommand:
    """Textual representation of a LaTeX command,
    generated from the elements of the Command object"""
    def __init__(self, cmd_obj):
        self.cmd_obj = cmd_obj
        self.name = cmd_obj.name
        self.comment = ''
        self.command = ''
        self.testcode = []
        self.init_templates()
        self.generate_comment()
        self.generate_cmd()
        self.generate_testcode()

    def generate_cmd(self):
        """Generates the core command"""
        tmpl = self.tmpl_cmd[self.cmd_obj.type]
        tmpl = tmpl.replace('CMD', self.cmd_obj.name)
        tmpl = tmpl.replace('ELEM', self.cmd_obj.element)
        tmpl = tmpl.replace('SCALE', self.cmd_obj.scale)
        tmpl = tmpl.replace('RAISE', self.cmd_obj.rais)
        self.command = tmpl

    def generate_comment(self):
        """Generates the comment"""
        for line in self.cmd_obj.comment:
            self.comment += '% ' + line + '\n'
        self.comment += lg.signature() + '\n'

    def generate_testcode(self):
        """Genrates a block of test code for the command"""
        self.testcode = self.tmpl_testcode.replace('CMD', self.cmd_obj.name)


    def init_templates(self):
        self.tmpl_cmd = {}
        self.tmpl_cmd['image'] = textwrap.dedent("""\
            \\newcommand*{\\CMDBase}[1][]{%
                \\setkeys{lilyDesignOptions}{scale=SCALE,raise=RAISE}%
                \\lilyPrintImage[#1]{ELEM}%
            }
            \\newcommand*{\\CMD}[1][]{\\CMDBase[#1] }
            \\WithSuffix\\newcommand\\CMD*[1][]{\\CMDBase[#1]}

            """)

        self.tmpl_cmd['glyphname'] = textwrap.dedent("""\
            \\newcommand*{\\CMDBase}[1][]{%
                \\setkeys{lilyDesignOptions}{scale=SCALE,raise=RAISE}%
                \\lilyPrint[#1]{\\lilyGetGlyph{ELEM}}%
            }
            \\newcommand*{\\CMD}[1][]{\\CMDBase[#1] }
            \\WithSuffix\\newcommand\\CMD*[1][]{\\CMDBase[#1]}

            """)

        self.tmpl_cmd['number'] = textwrap.dedent("""\
            \\newcommand*{\\CMDBase}[1][]{%
                \\setkeys{lilyDesignOptions}{scale=SCALE,raise=RAISE}%
                \\lilyPrint[#1]{\\lilyGetGlyphByNumber{ELEM}}%
            }
            \\newcommand*{\\CMD}[1][]{\\CMDBase[#1] }
            \\WithSuffix\\newcommand\\CMD*[1][]{\\CMDBase[#1]}

            """)

        self.tmpl_cmd['dynamics'] = textwrap.dedent("""\
            \\newcommand{\\CMDBase}[1][]{%
                \\mbox{%
                    \\lilyDynamics[#1]{ELEM}%
                }%
            }
            \\newcommand*{\\CMD}[1][]{\\CMDBase[#1] }
            \\WithSuffix\\newcommand\\CMD*[1][]{\\CMDBase[#1]}

            """)

        self.tmpl_cmd['text'] = textwrap.dedent("""\
            \\newcommand{\\CMDBase}[1][]{%
                \\setkeys{lilyDesignOptions}{scale=SCALE,raise=RAISE}%
                \\mbox{%
                    \\lilyText[#1]{ELEM}%
                }%
            }
            \\newcommand*{\\CMD}[1][]{\\CMDBase[#1] }
            \\WithSuffix\\newcommand\\CMD*[1][]{\\CMDBase[#1]}

            """)

        self.tmpl_testcode = textwrap.dedent("""\
            % CMD
            \\noindent\\textbf{\\textsf{Continuous text for} \\cmd{CMD}:}\\\\
            Lorem ipsum dolor sit amet, consectetur adipisicing elit,
            sed \\CMD do eiusmod tempor incididunt ut labore et dolore magna aliqua \\CMD*.\\\\
            \\CMD Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
            ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur\\CMD.
            \\CMD Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

            \\bigskip
            """)



