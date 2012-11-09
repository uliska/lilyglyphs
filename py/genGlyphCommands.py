#!/usr/bin/env python

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
# lilyglyphs_common.py                                                   #
#                                                                        #
# Common functionality for the Python scripts in lilyglyphs              #
#                                                                        #
# ########################################################################

import lilyglyphs_common as lg, os, sys

# ################
# Global variables

input_file = ''


def main(argv):
    check_argument(argv)
    lg.check_lilyglyphs_root()
    os.chdir(lg.dir_stash)
    lg.read_input_file(input_file)
    read_entries()
    
    #generate_latex_commands()
    
    
    
def check_argument(argv):
    global input_file
    try:
        input_file = str(argv[1])
    except:
        print 'An error occured with the argument:'
        print sys.exc_info()
        usage()
        sys.exit(1)

def generate_latex_commands():
    for cmd_name in lg.in_cmds:
        lg.generate_latex_command(cmd_name, lg.in_cmds[cmd_name][1])

def read_entries():
    for line in lg.definitions_file:
        line = line.strip()
        if len(line) == 0 or line[0] in '#%':
            continue
        print line
    
    # assign lg.in_cmds[cmd_name] = [comment (string), cmd_type (string)]
    
def usage():
    print 'genGlyphCommands.py'
    print 'is part of the lilyglyphs package'
    print ''
    print 'Usage:'
    print 'Pass the name (without path) of an input definitions file'
    print '(this has to be located in the /stash_new_commands directory.'
    print 'Please refer to the manual (documentation/lilyglyphs.pdf).'

# ####################################
# Finally launch the program
if __name__ == "__main__":
    main(sys.argv)
