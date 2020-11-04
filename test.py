import chord.voicing
import chord.instrument
import chord.render

formula = [0, 4, 7]
order = [0, 2, 0, 1]
strings = [0, 1, 2, 3]
inversion = 0
root = 5
tuning = [0, 5, 10, 15, 20, 25]

notes = chord.voicing.Voicing(formula, order=order, inversion=inversion, root=root)
gtr = chord.instrument.Instrument(tuning)
pos = gtr.play(notes, strings)
print(notes)
print(notes.octave)
print(*pos)
chord.render.to_text(pos)