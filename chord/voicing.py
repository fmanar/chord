from chord.chord import Chord
from chord.pitch import Pitch

class Voicing:
    '''An array-like set of tones decribing a chord voicing.

    Uses parallel arrays.  Pythonic?

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
            self._octave = [0 for _ in self._order]
            # build octaves the put each tone higher than last
            for i in range(1, len(self)):
                self._octave[i] = self._octave[i-1]
                if self._compute_pitch(i-1) > self._compute_pitch(i):
                    self._octave[i] += 1
        self._update()

    def _compute_pitch(self, i):
        index = self._order[i] + self._inversion
        chord_index = index % len(self.chord)
        octave_increment = index // len(self.chord)
        return (
            self.chord.root 
            + self.chord.formula[chord_index] 
            + 12*(self._octave[i] + octave_increment)
        )

    def _update(self):
        self._pitches = [self._compute_pitch(i) for i in range(len(self))]

    def __len__(self):
        return len(self.order)

    @property
    def pitches(self):
        return self._pitches

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
        self._update()
    
    @property
    def octave(self):
        return self._octave

    @octave.setter
    def octave(self, value):
        self._octave = value
        self._update()
    
    @property
    def inversion(self):
        return _inversion

    @inversion.setter
    def inversion(self, value):
        self._inversion = value
        self._update()