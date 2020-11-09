import unittest

from .context import chord
from chord.pitch import Pitch, PitchSequence

class TestPitch(unittest.TestCase):
    def test_init(self):
        p = Pitch(5)
        self.assertEqual(p.pitch, 5)

        p = Pitch("G#4")
        self.assertEqual(p.pitch, 68)

        p = Pitch("B")
        self.assertEqual(p.pitch, 11)

    def test_make(self):
        p1 = Pitch(7)
        p2 = Pitch.make(p1)
        self.assertIs(p1, p2)

        p3 = Pitch.make(7)
        self.assertEquals(p3.pitch, 7)

    def test_get_name(self):
        p = Pitch(61)
        self.assertEqual(p.get_name(), 'C#')
        self.assertEqual(p.get_name(absolute=True), 'C#4')
        self.assertEqual(p.get_name(flats=True), 'Db')

    def test_set_name(self):
        p = Pitch(0)
        p.set_name('Ab7')
        self.assertEqual(p.pitch, 104)

    def test_compare(self):
        p1 = Pitch(60)
        p2 = Pitch(60)
        self.assertEqual(p1, p2)
        self.assertEqual(p1, 60)
        self.assertEqual(p1, 'C4')

        p2 = Pitch(48)
        self.assertGreater(p1, p2)
        self.assertGreater(p1, 48)
        self.assertGreater(p1, 'C3')

        p2 = Pitch(72)
        self.assertLess(p1, p2)
        self.assertLess(p1, 72)
        self.assertLess(p1, 'C5')

    def test_arithmetic(self):
        p1 = Pitch(10)
        p2 = Pitch(7)
        a = p1 + p2
        b = p1 + 7
        self.assertEqual(a.pitch, 17)
        self.assertEqual(b.pitch, 17)

        a = p1 - p2
        b = p1 - 7
        self.assertEqual(a.pitch, 3)
        self.assertEqual(b.pitch, 3)
        
        a = 7 + p1
        b = 7 - p1
        self.assertEqual(a.pitch, 17)
        self.assertEqual(b.pitch, -3)

        p1 += 3
        self.assertEqual(p1.pitch, 13)

        p1 -= 5
        self.assertEqual(p1, 8)


class TestPitchSequence(unittest.TestCase):
    def test_init(self):
        ps = PitchSequence(Pitch(0))
        self.assertIsInstance(ps, PitchSequence)

        ps = PitchSequence([0, 4, 7])
        self.assertIsInstance(ps, PitchSequence)