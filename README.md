# chord
A chord chart generator for stringed instruments.  For the computing, inverting, finding, and displaying of chords.

## Structure
Pattern - a set of relative semitones defining the notes in the chord/scale.  Just a List of tones.
Voicing - an ordering of chord tones, inversion number, root. 
Instrument - defines string tunings
Frets - a listing of fretboard positions (i.e. a string+fret tuple)
    created from a voicing, instrument, and string selection.

## Defining Pitch
Pitches are denoted by integers counting half-steps.  0 is middle C (C4, MIDI note 60) by convention.