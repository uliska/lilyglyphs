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
# globals     .py                                                        #
#                                                                        #
# defines global variables                                               #
#                                                                        #
# ########################################################################

# ###############
# Directory names

# full path to the package's root directory
LILYGLYPHS_ROOT = ''
# root directory of the glyphimages stuff, relative to LILYGLYPHS_ROOT
GLYPH_IMG_ROOT = 'glyphimages'
# base directory for the output of the LaTeX files,
# relative to LILYGLYPHS_ROOT
D_STASH_ROOT = 'stash_new_commands'
# actual output directory, will be concatenated from
# LILYGLYPHS_ROOT and D_STASH_ROOT
# (absolute path, because it's generally outside the CWD)
D_STASH = ''
# The following are relative to CWD,
# which is usually set to GLYPH_IMG_ROOT when these are used
# base dir for the definitions input files 
D_DEFS = 'definitions'
# base dir for the generated LilyPond source files
D_SRC = 'generated_src'
# base dir for the generated (pdf) image files
D_IMG = 'generated_img'

# These constants are set at the beginning of the
# parsing of entries
DEF_RAISE = '0'
DEF_SCALE = '1'

