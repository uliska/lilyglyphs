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

Deploying considerations
========================
A deployable package should be a compressed archive that contains a subset of the files from the working tree.
It would be best to have a script that does this automatically, but for now we have to collect them by hand.

Folder structure
----------------
A folder **deploy** is located in the root directory of the working repository.  
For any new version of the package create a subfolder, named corresponding to the version (e.g. 0.1.2).  
We copy all relevant files to this directory and move them to archives in .tar.gz formats so that afterwards these archives are the only files in the directory.  
The archives should be named lilyglyphs_n.m.o (plus extension).

Included files
--------------
This list of files to include dates from version 0.0.5. If we fail to update this list please enclose any newer files at your discretion.

The archive should **include**:

- From the root dir:
    - CHANGES.md
    - COPYING
    - INSTALL.md
    - README.md
    - lilyglyphs.sty
    - lilyglyphsStyle.sty
- Complete subdirectories (any untracked files removed):
    - commands
    - core
    - glyphlist
    - otf
- Partial subdirectories (any untracked files removed):
    - documentation (only lilyglyphs.pdf)
    - glyphimages:
        - lilyglyphs_logo (only .pdf and .png)
        - pdfs (complete)

