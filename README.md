# chord
A chord chart generator for stringed instruments.  For the computing, inverting, finding, and displaying of chords.

## Structure
1. A chord/scale definition.  Describes the tones in a chord quality relative to root.
2. A voicing definition.  Describes order/repition of tones in a chord and assigns a root.
3. An instrument.  Describes strings and tunings.
4. Positions.  Describe locations on fretboard via string/fret pairs.

## Defining Pitch
Pitches are denoted by integers counting half-steps.  0 is middle C (C4, MIDI note 60) by convention.

## Todo
- create setup.py so pip can install
- make members of Voicing "properties" so that _update() is called when they change
- change positions and notes to dictionaries?
- allow extra attributes to be assigned to notes and carry through to rendering to allow for css-esque styling queues based on chord tone, finger, etc