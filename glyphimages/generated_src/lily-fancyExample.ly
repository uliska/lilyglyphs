
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

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                               %
% This file defines a single glyph to be created with LilyPond: %
%                                                               %
%   fancyExample.ly                                             %
%                                                               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% created by genImageCommands.py on 2013-09-07

\version "2.16.2"

#(set-global-staff-size 14)

\paper {
  indent = 0
}
\header {
  tagline = ""
}

%{
example of a fancy notation
%}

fancyExample = {
  \override NoteHead.transparent = ##t
  \override Stem #'length = #4
  \override Stem #'thickness = #1.6
  e4-.( e-. e-. e-.) \glissando
  s4 \stemDown a4 \laissezVibrer
}

  \score {
  \new Staff \with {
    \remove "Staff_symbol_engraver"
    \remove "Clef_engraver"
    \remove "Time_signature_engraver"
  }
  \fancyExample
}

