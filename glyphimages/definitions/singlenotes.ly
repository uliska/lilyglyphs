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
halfNoteDottedDown = {
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

%%lilyglyphs
% demisemiquaver with upward stem
%%protected
demisemiquaver = {
  \override Stem#'length = #7.5
  g'32
}

\markup { demisemiquaver }
symbol = \demisemiquaver
\include "score.ily"


%%lilyglyphs
% demisemiquaver with downward stem
%%protected
demisemiquaverDown = {
  \stemDown
  \override Stem#'length = #7.5
  g'32
}

%%lilyglyphs
% dotted demisemiquaver with upward stem
%%protected
demisemiquaverDotted = {
  \override Stem#'length = #7.5
  g'32.
}

\markup { demisemiquaverDotted }
symbol = \demisemiquaverDotted
\include "score.ily"

%%lilyglyphs
% dotted demisemiquaver with downward stem
%%protected
demisemiquaverDottedDown = {
  \stemDown
  \override Stem#'length = #7.5
  g'32.
}

%%lilyglyphs
% doubledotted demisemiquaver with upward stem
%%protected
demisemiquaverDottedDouble = {
  \override Stem#'length = #7.5
  g'32..
}

\markup { demisemiquaverDottedDouble }
symbol = \demisemiquaverDottedDouble
\include "score.ily"

%%lilyglyphs
% doubledotted demisemiquaver with downward stem
%%protected
demisemiquaverDottedDoubleDown = {
  \stemDown
  \override Stem#'length = #7.5
  g'32..
}
