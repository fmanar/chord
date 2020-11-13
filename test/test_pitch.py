import unittest

from .context import chord
from chord.pitch import pitchify, depitchify

class TestPitchify(unittest.TestCase):
    def test_single(self):
        p = pitchify('C')
        self.assertEqual(p, 0)
        p = pitchify('G3')
        self.assertEqual(p, 43)
        p = pitchify('G-2')
        self.assertEqual(p, -17)

    def test_sharp(self):
        p = pitchify('F#')
        self.assertEqual(p, 6)
        p = pitchify('A#2')
        self.assertEqual(p, 34)
        p = pitchify('A#-2')
        self.assertEqual(p, -14)

    def test_flat(self):
        p = pitchify('Gb')
        self.assertEqual(p, 6)
        p = pitchify('Bb2')
        self.assertEqual(p, 34)
        p = pitchify('Bb-2')
        self.assertEqual(p, -14)

    def test_tuple(self):
        p = pitchify(('C', 'E', 'G'))
        self.assertIsInstance(p, list)
        self.assertEqual(p[0], 0)
        self.assertEqual(p[1], 4)
        self.assertEqual(p[2], 7)

    def test_list(self):
        p = pitchify(['C', 'Eb', 'G'])
        self.assertIsInstance(p, list)
        self.assertEqual(p[0], 0)
        self.assertEqual(p[1], 3)
        self.assertEqual(p[2], 7)