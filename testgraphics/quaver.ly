\version "2.15.41"

symbol = {
  g'8
}
\paper {
  indent = 0
}
\header {
  tagline = ""
}

\score {
  \new Staff \with {
  \remove "Staff_symbol_engraver"
  \remove "Clef_engraver"
  \remove "Time_signature_engraver"
}
  \symbol 
}