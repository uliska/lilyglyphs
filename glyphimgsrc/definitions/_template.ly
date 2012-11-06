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

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This file defines a set of glyphs to be compiled in LilyPond %
%                                                              %
%   EXAMPLE                                                    %
%                                                              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\version "2.17.5"

%{ template for a single entry
   replace 'EXAMPLE_...' by actual content %}

% lilyglyphs entry
%%protected (use this line if you don't want the command to be generated)
%{ EXAMPLE_comment %}
EXAMPLE_command_name = {
  g'4
}

\markup { EXAMPLE_command_name }
symbol = \EXAMPLE_command_name
\include "score.ily"

% Example ends here
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

