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

import lilyglyphs_common as lg, os, sys,  getopt,  datetime,  subprocess

# ################
# Global variables

# flags
flag_force = False

# ###############
# string to be printed before the actual command
lily_src_prefix = """\\version "2.17.4"

#(set-global-staff-size 14)

\paper {
  indent = 0
}
\header {
  tagline = ""
}

"""

# string to be printed after the actual command definition
lily_src_score = """
  \\score {
  \\new Staff \\with {
    \\remove "Staff_symbol_engraver"
    \\remove "Clef_engraver"
    \\remove "Time_signature_engraver"
  }
"""

def main(argv):
    global flag_force, definitions_file_name
    short_options = 'i:'
    long_options = []
    long_options.append('input=')
    try:
        opts, args = getopt.getopt(argv, short_options, long_options)
        for opt, arg in opts:
            if opt in ("-i",  "--input"):
                lg.input_files.append(arg)
            else:
                usage()
                sys.exit(2)
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    # Do the actual work of the script
    print ''
    print 'buildglyphimages.py,'
    print 'Part of lilyglyphs.'

    print ''
    check_paths()

    for input_file_name in lg.input_files:
        print ''
        lg.read_input_file('definitions/' + input_file_name)
        
        basename, dummy = os.path.splitext(input_file_name)
        lg.cat_subdir = basename + '/'

        print ''
        read_entries()

        print ''
        write_lily_src_files()

        print ''
        lg.compile_lily_files()

        print ''
        lg.generate_latex_commands()

    print ''
    lg.cleanup_lily_files()

    print ''
    write_latex_file()


def check_paths():
    """Sets CWD to 'glyphimages' subdir
       and makes sure that the necessary subdirectories are present"""
    global lilyglyphs_root
    lg.check_lilyglyphs_root()
    os.chdir('glyphimages')

    # check the presence of the necessary subdirectories
    # and create them if necessary
    # (otherwise we'll get errors when trying to write in them)
    ls = os.listdir('.')
    if not 'generated_src' in ls:
        os.mkdir('generated_src')
    if not 'pdfs' in ls:
        os.mkdir('pdfs')
    if not os.path.exists(lg.dir_stash):
        os.mkdir(lg.dir_stash)
    if not os.path.exists(lg.dir_stash + 'images'):
        os.mkdir(lg.dir_stash + 'images')

def read_entries():
    """Parses the input source file and extracts glyph entries"""
    print 'Read entries of LilyPond commands:'
    for i in range(len(lg.definitions_file)):
        if '%%lilyglyphs' in lg.definitions_file[i]:
            i = read_entry(i)

def read_entry(i):
    """Reads a single glyph entry from the input file and stores it
    in the global dictionary lg.in_cmds"""
    # read comment line(s)
    i += 1
    is_protected = False
    comment = []
    # loop over the comment line(s)
    while i < len(lg.definitions_file):
        line = lg.definitions_file[i].strip()
        # check for 'protected' entries that shouldn't be processed newly
        if not line[0] == '%':
            break
        elif '%%protected' in line:
            is_protected = True
        else:
            line = line[1:].strip()
            comment.append(line)
        i += 1

    # remove any empty lines
    while len(lg.definitions_file[i].strip()) == 0:
        i += 1
    
    # read command name
    line = lg.definitions_file[i].strip()
    cmd_name = line[: line.find('=') - 1]
    print '- ' + cmd_name, 
    if is_protected:
        print '(protected and skipped)'
    else:
        print '' #(for line break only)
        
    # read actual command until we find a line the begins with a closing curly bracket
    i += 1
    lilySrc = []
    while lg.definitions_file[i][0] != '}':
        lilySrc.append(lg.definitions_file[i])
        i += 1
    if not is_protected:
        lg.in_cmds[cmd_name] = {}
        lg.in_cmds[cmd_name]['comment'] = comment
        lg.in_cmds[cmd_name]['lilySrc'] = lilySrc
        lg.in_cmds[cmd_name]['element'] = cmd_name
        lg.in_cmds[cmd_name]['type'] = 'image'
        
        lg.lily_files.append((lg.cat_subdir, cmd_name))
    return i


def usage():
    print """buildglyphimages. Part of the lilyglyphs package.
    Parses a .lysrc (lilyglyphs source) file, creates
    single .ly files from it, uses LilyPond to create single glyph
    pdf files and set up template files to be used in LaTeX.
    For detailed instructions refer to the manual.
    Usage:
    -i filename --input=filename (mandatory): Specifies the input file.
    -f --force: overwrite files if they already exist
    """

def write_file_info(name, fout):
    """Formats file specific information for the lilyPond source file"""
    long_line = '% This file defines a single glyph to be created with LilyPond: %\n'
    width = len(long_line) - 1
    header = '%' * width + '\n'
    spacer = '%' + ' ' * (width - 2) + '%\n'
    padding = width - len(name) - 8
    fout.write(header)
    fout.write(spacer)
    fout.write(long_line)
    fout.write(spacer)
    fout.write('%   ' + name + '.ly' + ' ' * padding + '%\n')
    fout.write(spacer)
    fout.write(header)
    fout.write(lg.signature())
    fout.write('\n\n')

def write_latex_file():
    """Composes LaTeX file and writes it to disk"""
    print 'Generate LaTeX file'
    lg.write_latex_file('images/newImageGlyphs.tex')

def write_lily_src_files():
    """Generates one .ly file for each found new command"""
    print 'Write .ly files for each entry:'
    src_dir = lg.dir_lysrc + lg.cat_subdir[:-1]
    if not os.path.exists(src_dir):
        os.mkdir(src_dir)
    for cmd_name in lg.in_cmds:
        print '- ' + cmd_name
        # open a single lily src file for write access
        fout = open(src_dir + '/' + cmd_name + '.ly',  'w')

        #output the license information
        fout.write(lg.lilyglyphs_copyright_string)
        fout.write('\n')

        #output information on the actual file
        write_file_info(cmd_name, fout)

        #write the default LilyPond stuff
        fout.write(lily_src_prefix)

        # write the comment for the command
        fout.write('%{\n')
        for line in lg.in_cmds[cmd_name]['comment']:
            fout.write(line + '\n')
        fout.write('%}\n\n')

        # write the actual command
        fout.write(cmd_name + ' = {\n')
        for line in lg.in_cmds[cmd_name]['lilySrc']:
            fout.write(line + '\n')
        fout.write('}\n')

        # write the score definition
        fout.write(lily_src_score)

        # finish the LilyPond file
        fout.write('  \\' + cmd_name + '\n')
        fout.write('}\n\n')

        fout.close()

# ####################################
# Finally launch the program
if __name__ == "__main__":
    main(sys.argv[1:])
