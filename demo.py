from chord.pitch import Pitch, PitchSequence
from chord.chord import Chord
from chord.voicing import Voicing
from chord.instrument import Instrument
from chord.render import to_text

root = Pitch('G')
formula = PitchSequence([0, 4, 7])
order = [0, 2, 1]
strings = [0, 1, 3]
inversion = 0
tuning = [0, 5, 10, 15, 20, 25]

chord = Chord(formula, root=root)
voicing = Voicing(chord, order=order, inversion=inversion)
gtr = Instrument(tuning)
pos = [gtr.play(n, s) for n, s in zip(voicing, strings)]
print('Chord', voicing.chord)
print('Order', voicing.order)
print('Octave', voicing.octave)
print('Voicing', voicing)
print('Positions', *pos)
to_text(pos)