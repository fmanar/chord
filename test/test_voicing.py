import unittest

from .context import chord
from chord.pitch import Pitch, PitchSequence
from chord.chord import Chord
from chord.voicing import Voicing

class TestVoicing(unittest.TestCase):
    def test_init(self):
        c = Chord(PitchSequence([0, 4, 7]))
        v = Voicing(c)
        self.assertIsInstance(v, Voicing)

        v = Voicing(c, order=[0, 2, 1])
        self.assertEqual(v[0], c[0])
        self.assertEqual(v[1], c[2])
        self.assertEqual(v[2], c[1] + 12)

        v = Voicing(c, order=[0, 2, 1], octave=[0, 0, 2])
        self.assertEqual(v[0], c[0])
        self.assertEqual(v[1], c[2])
        self.assertEqual(v[2], c[1] + 24)

        v = Voicing(c, order=[0, 2, 1], octave=[0, 0, 2], inversion=1)
        self.assertEqual(v[0], c[1])
        self.assertEqual(v[1], c[0] + 12)
        self.assertEqual(v[2], c[2] + 24)