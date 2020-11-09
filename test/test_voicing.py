import unittest

from .context import chord
from chord.pitch import Pitch
from chord.chord import Chord
from chord.voicing import Voicing

class TestVoicing(unittest.TestCase):
    def test_init(self):
        c = Chord([0, 4, 7])
        v = Voicing(c)
        self.assertIsInstance(v, Voicing)

        v = Voicing(c, order=[0, 2, 1])
        self.assertEqual(v.pitches[0], c.pitches[0])
        self.assertEqual(v.pitches[1], c.pitches[2])
        self.assertEqual(v.pitches[2], c.pitches[1] + 12)

        v = Voicing(c, order=[0, 2, 1], octave=[0, 0, 2])
        self.assertEqual(v.pitches[0], c.pitches[0])
        self.assertEqual(v.pitches[1], c.pitches[2])
        self.assertEqual(v.pitches[2], c.pitches[1] + 24)

        v = Voicing(c, order=[0, 2, 1], octave=[0, 0, 2], inversion=1)
        self.assertEqual(v.pitches[0], c.pitches[1])
        self.assertEqual(v.pitches[1], c.pitches[0] + 12)
        self.assertEqual(v.pitches[2], c.pitches[2] + 24)