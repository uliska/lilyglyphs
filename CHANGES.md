    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
    %                                                                        %  
    %      This file is part of the 'lilyglyphs' LaTeX package.              %  
    %                                ==========                              %  
    %                                                                        %  
    %              https://github.com/uliska/lilyglyphs                      %  
    %                                                                        %  
    %  Copyright 2012 by Urs Liska, git@ursliska.de                          %  
    %                                                                        %  
    %  'lilyglyphs' is free software: you can redistribute it and/or modify  %  
    %  it under the terms of the GNU General Public License as published by  %  
    %  the Free Software Foundation, either version 3 of the License, or     %  
    %  (at your option) any later version.                                   %  
    %                                                                        %  
    %  This program is distributed in the hope that it will be useful,       %  
    %  but WITHOUT ANY WARRANTY; without even the implied warranty of        %  
    %  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          %  
    %  GNU General Public License for more details.                          %  
    %                                                                        %  
    %  You should have received a copy of the GNU General Public License     %  
    %  along with this program.  If not, see <http://www.gnu.org/licenses/>. %  
    %                                                                        %  
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  

*lilyglyphs* - Release Notes
============================
This document lists all changes in the development of *lilyglyphs*.  
All changes should be present in the manual, but only the finished versions printed bold are available as pdf downloads. (Latest changes are only found in the master branch of the git repository. They should be documentd in the lilyglyphs.tex file there too.)
So the lines above the topmost bold version line represent the changes not available in the downloadable pdf documentation.

- Pyhton script buildglyphimages.py  
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