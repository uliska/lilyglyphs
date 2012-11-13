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
%%lilyglyphs
%%protected (use this line if you don't want the command to be generated)
% EXAMPLE_comment
EXAMPLE_command_name = {
  g'4
}

\markup { EXAMPLE_command_name }
symbol = \EXAMPLE_command_name
\include "score.ily"

% Example ends here
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%lilyglyphs
% half note with upward stem
%%protected
halfNote = {
  \override Stem#'length = 5
  g'2
}

\markup { halfNote }
symbol = \halfNote
\include "score.ily"

%%lilyglyphs
% half note with downward stem
% scale=0.75
% raise=-0.4
%%protected
halfNoteDown = {
  \stemDown
  \override Stem#'length = 5
  g'2
}

%%lilyglyphs
% dotted half note with upward stem
%%protected
halfNoteDotted = {
  \override Stem#'length = 5
  g'2.
}

\markup { halfNoteDotted }
symbol = \halfNoteDotted
\include "score.ily"

%%lilyglyphs
% dotted half note with downward stem
%%protected
halfNoteDottedDown = {#
  \stemDown
  \override Stem#'length = 5
  g'2.
}

%%lilyglyphs
% doubledotted half note with upward stem
%%protected
halfNoteDottedDouble = {
  \override Stem#'length = 5
  g'2..
}

\markup { halfNoteDottedDouble }
symbol = \halfNoteDottedDouble
\include "score.ily"

%%lilyglyphs
% doubledotted half note with downward stem
%%protected
halfNoteDottedDoubleDown = {
  \stemDown
  \override Stem#'length = 5
  g'2..
}

%%lilyglyphs
% crotchet with upward stem
%%protected
crotchet = {
  \override Stem#'length = 5
  g'4
}

\markup { crotchet }
symbol = \crotchet
\include "score.ily"

%%lilyglyphs
% crotchet with downward stem
%%protected
crotchetDown = {
  \stemDown
  \override Stem#'length = 5
  g'4
}

%%lilyglyphs
% dotted crotchet with upward stem
%%protected
crotchetDotted = {
  \override Stem#'length = 5
  g'4.
}

\markup { crotchetDotted }
symbol = \crotchetDotted
\include "score.ily"

%%lilyglyphs
% dotted crotchet with downward stem
%%protected
crotchetDottedDown = {
  \stemDown
  \override Stem#'length = 5
  g'4.
}

%%lilyglyphs
% doubledotted crotchet with upward stem
%%protected
crotchetDottedDouble = {
  \override Stem#'length = 5
  g'4..
}

\markup { crotchetDottedDouble }
symbol = \crotchetDottedDouble
\include "score.ily"


%%lilyglyphs
% doubledotted crotchet with upward stem
%%protected
crotchetDottedDoubleDown = {
  \stemDown
  \override Stem#'length = 5
  g'4..
}

%%lilyglyphs
% quaver with upward stem
%%protected
quaver = {
  \override Stem#'length = 6
  g'8
}

%%lilyglyphs
% quaver with downward stem
%%protected
quaverDown = {
  \stemDown
  \override Stem#'length = 6
  g'8
}

\markup { quaver }
symbol = \quaver
\include "score.ily"

%%lilyglyphs
% dotted quaver with upward stem
quaverDotted = {
  \override Stem#'length = 6
  g'8.
}

\markup { quaverDotted }
symbol = \quaverDotted
\include "score.ily"


%%lilyglyphs
% dotted quaver with downward stem
%%protected
quaverDottedDown = {
  \stemDown
  \override Stem#'length = 6
  g'8.
}

%%lilyglyphs
% doubledotted quaver with upward stem
quaverDottedDouble = {
  \override Stem#'length = 6
  g'8..
}

\markup { quaverDottedDouble }
symbol = \quaverDottedDouble
\include "score.ily"

%%lilyglyphs
% doubledotted quaver with downward stem
%%protected
quaverDottedDoubleDown = {
  \stemDown
  \override Stem#'length = 6
  g'8..
}

%%lilyglyphs
% semiquaver with upward stem
%%protected
semiquaver = {
  \override Stem#'length = #6.5
  g'16
}

\markup { semiquaver }
symbol = \semiquaver
\include "score.ily"


%%lilyglyphs
% semiquaver with downward stem
%%protected
semiquaverDown = {
  \stemDown
  \override Stem#'length = #6.5
  g'16
}

%%lilyglyphs
% dotted semiquaver with upward stem
%%protected
semiquaverDotted = {
  \override Stem#'length = #6.5
  g'16.
}

\markup { semiquaverDotted }
symbol = \semiquaverDotted
\include "score.ily"

%%lilyglyphs
% dotted semiquaver with downward stem
%%protected
semiquaverDottedDown = {
  \stemDown
  \override Stem#'length = #6.5
  g'16.
}

%%lilyglyphs
% doubledotted semiquaver with upward stem
%%protected
semiquaverDottedDouble = {
  \override Stem#'length = #6.5
  g'16..
}

\markup { semiquaverDottedDouble }
symbol = \semiquaverDottedDouble
\include "score.ily"

%%lilyglyphs
% doubledotted semiquaver with downward stem
%%protected
semiquaverDottedDoubleDown = {
  \stemDown
  \override Stem#'length = #6.5
  g'16..
}

    