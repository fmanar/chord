import unittest

from .context import chord
from chord.chord import Chord
from chord.pitch import pitchify

class TestChord(unittest.TestCase):
    def test_simple(self):
        c = Chord([0, 4, 7])
        self.assertEqual(c.pitches[0], 0)
        self.assertEqual(c.pitches[1], 4)
        self.assertEqual(c.pitches[2], 7)

    def test_root(self):
        c = Chord([0, 4, 7], root=pitchify('E'))
        self.assertEqual(c.root, pitchify('E'))
        self.assertEqual(c.formula[0], 0)
        self.assertEqual(c.formula[1], 4) 
        self.assertEqual(c.formula[2], 7)
        self.assertEqual(c.pitches[0], 4)
        self.assertEqual(c.pitches[1], 8)
        self.assertEqual(c.pitches[2], 11)
