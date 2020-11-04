import chord

class Voicing(Chord):
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
            self._order = [i for i in range(len(chord))]
            
        if octave:
            self._octave = octave
        else:
            self._octave = [0 for _ in self._order]
            # build octaves the put each tone higher than last
            for i in range(1, len(self._order)):
                self._octave[i] = self._octave[i-1]
                if ((self.chord[self._order[i-1]] + 12*self._octave[i-1]) 
                        > (self.chord[self._order[i]] + 12*self._octave[i])):
                    self._octave[i] += 1

        self._inversion = inversion
        self._compute_notes()

    def _compute_notes(self):
        for i in range(len(self._order)):
            index = (self._order[i] + self._inversion) % len(self.chord)
            value = self.chord.root + self.chord[index] + 12*self._octave[i]
            self._notes.append(Note(value))

    @property
    def notes(self):
        return _notes

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
        self._compute_notes()
    
    @property
    def octave(self):
        return _octave

    @octave.setter
    def octave(self, value):
        self._octave = value
        self._compute_notes()
    
    @property
    def inversion(self):
        return _inversion

    @inversion.setter
    def inversion(self, value):
        self._inversion = value
        self._compute_notes()