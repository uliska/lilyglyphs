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
# command.py                                                             #
#                                                                        #
# defines the class Command                                              #
# which represents the properties of one command.                        #
# The class doesn't implement any functionality                          #
#                                                                        #
# ########################################################################

from latexcommand import LatexCommand

class Command:
    """Represents a lilyglyphs command.
    Holds input definitions, LilyPond source code and LaTeX commands."""
    def __init__(self, name):
        # command name
        self._name = name
        # comment used for the command
        self._comment = []
        # content element to be passed to the printing command (in LaTeX)
        self._element = ''
        # type of command, specifies which printing command LaTeX uses
        # and which code template the script uses.
        self._type = ''
        # default scaling that is included in the command definition
        self._scale = ''
        # default raise value for the command definition
        self._raise = ''
        # LilyPond source code (only has content with image driven glyphs)
        self._lilySrc = []
        # object that holds LaTeX representations of the command (cmd, comment and testcode)
        self._latex_cmd = None
        # textual LilyPond  representation of the command
        self._lilypond_cmd = []

    # properties

    # comment
    def _get_comment(self):
        return self._comment
    comment = property(fget = _get_comment)

    # element
    def _get_element(self):
        return self._element
    element = property(fget = _get_element)

    # scale
    def _get_scale(self):
        return self._scale
    scale = property(fget = _get_scale)

    # type
    def _get_type(self):
        return self._type
    type = property(fget = _get_type)

       # raise
    def _get_raise(self):
        return self._raise
    rais = property(fget = _get_raise)

    # name
    def _get_name(self):
        return self._name
    name = property(fget = _get_name)

    def get_latex_cmd(self):
        return self._latex_cmd
    latex_cmd = property(fget = get_latex_cmd)

    def set_comment(self, comment):
        self._comment = comment

    def set_element(self,  element):
        self._element = str(element)

    def set_latex_cmd(self, ltx_cmd):
        if not isinstance(ltx_cmd, LatexCommand):
            raise TypeError('Not a LatexCommand instance')#
        self._latex_cmd = ltx_cmd

    def set_lilypond_cmd(self, lily_cmd):
        self._lilypond_cmd = lily_cmd

    def set_lilySrc(self, lilySrc):
        self._lilySrc = lilySrc

    def set_name(self, name):
        self._name = str(name)

    def set_raise(self, rais):
        self._raise = str(rais)

    def set_scale(self, scale):
        self._scale = str(scale)

    def set_type(self, type):
        self._type = str(type)

