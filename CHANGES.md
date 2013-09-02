%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                        %
%      This file is part of the 'lilyglyphs' LaTeX package.              %
%                                ==========                              %
%                                                                        %
%              https://github.com/openlilylib/lilyglyphs                 %
%               http://www.openlilylib.org/lilyglyphs                    %
%                                                                        %
%  Copyright 2012-2013 Urs Liska and others, ul@openlilylib.org          %
%                                                                        %
%  'lilyglyphs' is free software: you can redistribute it and/or modify  %
%  it under the terms of the LaTeX Project Public License, either        %
%  version 1.3 of this license or (at your option) any later version.    %
%  You may find the latest version of this license at                    %
%               http://www.latex-project.org/lppl.txt                    %
%  more information on                                                   %
%               http://latex-project.org/lppl/                           %
%  and version 1.3 or later is part of all distributions of LaTeX        %
%  version 2005/12/01 or later.                                          %
%                                                                        %
%  This work has the LPPL maintenance status 'maintained'.               %
%  The Current Maintainer of this work is Urs Liska (see above).         %
%                                                                        %
%  This work consists of the files listed in the file 'manifest.txt'     %
%  which can be found in the 'license' directory.                        %
%                                                                        %
%  This program is distributed in the hope that it will be useful,       %
%  but WITHOUT ANY WARRANTY; without even the implied warranty of        %
%  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  %
%                                                                        %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

*lilyglyphs* - Release Notes
============================
This document lists all changes in the development of *lilyglyphs*.  
All changes should be present in the manual, but only the finished versions printed bold are available as pdf downloads. (Latest changes are only found in the master branch of the git repository. They should be documentd in the lilyglyphs.tex file there too.)
So the lines above the topmost bold version line represent the changes not available in the downloadable pdf documentation.

- lilyglyphs now also works with LuaLaTeX!  
  (Thanks to Dave Bellows)
- considerable revision of the manual
- Provide 'private' directory to add personal commands
- pdf files for image based commands are now tracked in the Git repository
- some modifications to the use of the Python scripts
- Drop support/necessity for starred commands  
  All commands by default now don't print a space after them.
  To achieve that effect one has to write a pair of curly braces.  
  This is in line with default behaviour of e.g \LaTeX{} and similar commands
- The command generation scripts accept scale= and raise= entries that set default values for subsequent commands
- Fix \lilyTimeSignature  
Now scales correctly and doesn't have a fraction line anymore.  
'raise' still doesn't work.

0.2.0
-----
(2012-11-10)

- Add some commands with images, mainly single notes.
- graphical \lilyglyphs command with corresponding .pdf and .png files
- Python script rebuild-pdfs.py  
Re-creates pdf files for use in image driven commands that are missing because they are not tracked in Git
Python script deploy.py  
Gathers the relevant files and puts them in an archive
- Python script genGlyphCommands.py  
Very easy way to create new commands with arbitrary sources.
- Python script buildglyphimages.py  
Very easy way to create new image glyphs and their respective commands
at the same time. You can edit the objects in LilyPond, then
let the script do the rest: write LilyPond source files, compile the image files,
create LaTeX commands, a documentation table and test code for fine-tuning the commands.
- New generic commands \lilyPrintImage and \lilyImage  
(loading 'glyphs' from PDF images created with LilyPond)

0.1.0
-----
(2012-10-19)

- Add dotted symbols and the logic behind it
- Add some rest glyphs
- Add fermata
- Add all 'sharp' accidentals

0.0.5
-----
(2012-09-25)

- Exchange meaning of starred and unstarred command versions:  
Unstarred now means: with trailing space (continuous text),  
starred means: without trailing space
- Implement numerical time signatures  
(scaling and vertical placement don't work properly yet)
- Plus: Major rewrite of the manual

0.0.2 
-----
(2012-09-23)

- New syntax accepting key=value options for generic and predefined commands.
- Options can be set at global, design time and command invocation level.
- Optical sizes of the Emmentaler font can be selected

0.0.1
-----
(2012-09-06)

- All glyphs from Emmentaler can be printed using generic access commands
- Some predefined commands are already available.
