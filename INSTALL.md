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

Installation instructions
=========================
Installation of the *lilyglyphs* package may vary according to your operating system and LaTeX distribution.
Therefore this file only gives some hints on what you have to achieve.
For sligthly more detailed instructions please refer to the pdf manual.

Requirements
------------
This package is based on OpenType font access through the *fontspec* package.
Therefore you can use it only with a LaTeX flavor that supports fontspec.
*lilyglyphs* has been developped using XeLaTeX, but it should also work with LuaLaTeX (untested).

LaTeX package
-------------
Extract the whole archive to a place where LaTeX can find it.

OpenType fonts
--------------
The .otf files that are located in the 'otf' subfolder of the package have to be made visible to fontspec. Please refer to the documentation of fontspec, LaTeX and your operating system.