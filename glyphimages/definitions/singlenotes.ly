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
%   Single notes                                               %
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

% lilyglyphs entry
%%protected 
%{ half note with upward stem %}
halfNote = {
  \override Stem#'length = 5
  g'2
}

\markup { halfNote }
symbol = \halfNote
\include "score.ily"

% lilyglyphs entry
%{ dotted half note with upward stem %}
halfNoteDotted = {
  \override Stem#'length = 5
  g'2.
}

\markup { halfNoteDotted }
symbol = \halfNoteDotted
\include "score.ily"

% lilyglyphs entry
%%protected 
%{ crotchet with upward stem %}
crotchet = {
  \override Stem#'length = 5
  g'4
}

\markup { crotchet }
symbol = \crotchet
\include "score.ily"

% lilyglyphs entry
%{ dotted crotchet with upward stem %}
crotchetDotted = {
  \override Stem#'length = 5
  g'4.
}

\markup { crotchetDotted }
symbol = \crotchetDotted
\include "score.ily"


% lilyglyphs entry
%%protected 
%{ quaver with upward stem %}
quaver = {
  \override Stem#'length = 6
  g'8
}

\markup { quaver }
symbol = \quaver
\include "score.ily"

% lilyglyphs entry
%{ dotted quaver with upward stem %}
quaverDotted = {
  \override Stem#'length = 6
  g'8.
}

\markup { quaverDotted }
symbol = \quaverDotted
\include "score.ily"


% lilyglyphs entry
%%protected 
%{ semiquaver with upward stem %}
semiquaver = {
  \override Stem#'length = #6.5
  g'16
}

\markup { semiquaver }
symbol = \semiquaver
\include "score.ily"

% lilyglyphs entry
%{ dotted semiquaver with upward stem %}
semiquaverDotted = {
  \override Stem#'length = #6.5
  g'16.
}

\markup { semiquaverDotted }
symbol = \semiquaverDotted
\include "score.ily"

