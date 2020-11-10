import unittest

from .context import chord
from chord.chord import Chord
from chord.pitch import Pitch, PitchSequence

class TestChord(unittest.TestCase):
    def test_init(self):
        c = Chord(PitchSequence([Pitch(0), Pitch(4), Pitch(7)]))
        self.assertEqual(c[0], 0)
        self.assertEqual(c[1], Pitch(4))
        self.assertEqual(c[2], 'G')

        c = Chord(PitchSequence([0, 4, 7]))
        self.assertEqual(c[0], 0)
        self.assertEqual(c[1], Pitch(4))
        self.assertEqual(c[2], 'G')

        c = Chord(PitchSequence(['C', 'E', 'G']))
        self.assertEqual(c[0], 0)
        self.assertEqual(c[1], Pitch(4))
        self.assertEqual(c[2], 'G')

        c = Chord(PitchSequence(['D', 'F#', 'A']))
        self.assertEqual(c.root, Pitch(2))
        self.assertEqual(c.formula[0], 0)
        self.assertEqual(c.formula[1], 4)
        self.assertEqual(c.formula[2], 7)
        self.assertEqual(c[0], 2)
        self.assertEqual(c[1], 6)
        self.assertEqual(c[2], 9)

        c = Chord(PitchSequence(['D', 'F#', 'A']), root=Pitch('E'))
        self.assertEqual(c.root, Pitch('E'))
        self.assertEqual(c.formula[0], -2)
        self.assertEqual(c.formula[1], 2) 
        self.assertEqual(c.formula[2], 5)
        self.assertEqual(c[0], 2)
        self.assertEqual(c[1], 6)
        self.assertEqual(c[2], 9)
