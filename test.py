import chord.voicing
import chord.instrument
import chord.render

notes = chord.voicing.Voicing([0, 7, 0, 4], inversion=0)
gtr = chord.instrument.Instrument([0, 5, 10, 15, 20, 25])
pos = gtr.play(notes, [0, 1, 2, 3])
print(notes)
print(*pos)
chord.render.to_text(pos)