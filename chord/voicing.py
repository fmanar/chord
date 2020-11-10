from chord.chord import Chord
from chord.pitch import Pitch, PitchSequence

class Voicing(PitchSequence):
    '''An array-like set of tones decribing a chord voicing.

    Attributes:
        chord (Chord): the chord or scale tones.
        order (list of int): the ordering of the formula tones as formula 
            indexes.  If not supplied, the order defaults to the formula.
        octave (list of int): the relative octave to place the formula tones in 
            as a parallel array with order.  If not supplied, defaults to 
            whatever is required to make the pitch sequence monotonically 
            increasing.
        inversion (int): sets the formula tone increment
    '''
    def __init__(self, chord, order=None, octave=None, inversion=0, attrib={}):
        self.chord = chord
        if order:
            self._order = order
        else:
            self._order = [i for i in range(len(self.chord))]
        self._inversion = inversion
        if octave:
            self._octave = octave
        else:
            # build octaves the put each tone higher than last
            self._octave = []
            last = None
            for ord in self._order:
                curr = self.chord[ord]
                if not last:
                    self._octave.append(0)
                elif last > curr:
                    self._octave.append(1)
                else:
                    self._octave.append(self._octave[-1])
                last = curr
                
        self._pitches = []
        for ord, oct in zip(self._order, self._octave):
            index = ord + self._inversion
            chord_index = index % len(self.chord)
            octave_increment = index // len(self.chord)
            self._pitches.append(
                self.chord.root 
                + self.chord.formula[chord_index] 
                + 12*(oct + octave_increment)
            )

    @property
    def order(self):
        return self._order

    @property
    def octave(self):
        return self._octave

    @property
    def inversion(self):
        return _inversion
