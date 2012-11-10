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
# genGlyphCommands.py                                                    #
#                                                                        #
# generate commands based on Emmentaler glyphs                           #
#                                                                        #
# ########################################################################

import lilyglyphs_common as lg, os, sys

def main(input_file):
    lg.check_lilyglyphs_root()
    os.chdir(lg.dir_stash)
    if not os.path.exists('emmentaler'):
        os.mkdir('emmentaler')
    os.chdir('emmentaler')
    lg.read_input_file(input_file)
    read_entries()
    
    lg.generate_latex_commands()
    
    lg.write_latex_file('emmentaler/newGlyphCommands.tex')
    
    
def read_entries():
    entry = {}
    def reset_entry():
        entry['cmd'] = ''
        entry['element'] = ''
        entry['type'] = 'glyphname'
        entry['comment'] = []
    
    reset_entry()
    for line in lg.definitions_file:
        line = line.strip()
        # empty line = end of entry
        if not len(line):
            # skip if cmd and glyph haven't been filled both
            if not (entry['cmd'] and entry['element']):
                print 'Skip malformed entry \'' + entry['cmd'] + '\'. Please check input file'
                reset_entry()
            else:
                print 'Read entry \'' + entry['cmd'] + '\''
                lg.in_cmds[entry['cmd']] = {}
                lg.in_cmds[entry['cmd']]['element'] = entry['element']
                lg.in_cmds[entry['cmd']]['type'] = entry['type']
                lg.in_cmds[entry['cmd']]['comment'] = entry['comment']
                reset_entry()
        # ignore Python or LaTeX style comments
        elif line[0] in '#%':
            continue
        else:
            keyval = line.split('=')
            if keyval[0] == 'comment':
                entry['comment'] = [keyval[1]]
            else:
                entry[keyval[0].strip()] = keyval[1].strip()

    
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
    if len(sys.argv) < 2:
        print 'No filename argument given.\n'
        usage()
        sys.exit(2)
    main(sys.argv[1])
