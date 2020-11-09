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