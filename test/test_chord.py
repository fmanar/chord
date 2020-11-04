import unittest

from .context import chord
from chord.chord import Chord
from chord.pitch import Pitch

class TestChord(unittest.TestCase):
    def test_init(self):
        c = Chord([Pitch(0), Pitch(4), Pitch(7)])
        self.assertEqual(c.pitches[0], 0)
        self.assertEqual(c.pitches[1], Pitch(4))
        self.assertEqual(c.pitches[2], 'G')

        c = Chord([0, 4, 7])
        self.assertEqual(c.pitches[0], 0)
        self.assertEqual(c.pitches[1], Pitch(4))
        self.assertEqual(c.pitches[2], 'G')

        c = Chord(['C', 'E', 'G'])
        self.assertEqual(c.pitches[0], 0)
        self.assertEqual(c.pitches[1], Pitch(4))
        self.assertEqual(c.pitches[2], 'G')

        c = Chord(['D', 'F#', 'A'])
        self.assertEqual(c.root, Pitch(2))
        self.assertEqual(c.formula[0], 0)
        self.assertEqual(c.formula[1], 4)
        self.assertEqual(c.formula[2], 7)
        self.assertEqual(c.pitches[0], 2)
        self.assertEqual(c.pitches[1], 6)
        self.assertEqual(c.pitches[2], 9)

        c = Chord(['D', 'F#', 'A'], root='E')
        self.assertEqual(c.root, Pitch('E'))
        self.assertEqual(c.formula[0], -2)
        self.assertEqual(c.formula[1], 2) 
        self.assertEqual(c.formula[2], 5)
        self.assertEqual(c.pitches[0], 2)
        self.assertEqual(c.pitches[1], 6)
        self.assertEqual(c.pitches[2], 9)

    def test_str(self):
        c = Chord(['D', 'F#', 'A'])
        self.assertEqual(str(c), '[2, 6, 9]')