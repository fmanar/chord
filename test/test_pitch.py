import unittest

from .context import chord
import chord.pitch

class TestPitch(unittest.TestCase):
    def test_constructor_int(self):
        p = chord.pitch.Pitch(5)
        self.assertEqual(p.pitch, 5)

    def test_constructor_str(self):
        p = chord.pitch.Pitch("G#4")
        self.assertEqual(p.pitch, 68)