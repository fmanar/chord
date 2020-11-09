from .pitch import Pitch, PitchSequence

class Chord(PitchSequence):
    '''An ordered collection of pitches relative to a root.

    Can be either an absolute chord or a relative formula. The pitches are
    assumed to be monotonically increasing, though this isn't enforced. Can
    be constructed by specifying the formula or pitches.

    Examples:
        >>> c = Chord([Pitch(0), Pitch(4), Pitch(7)]) # major triad
        >>> c = Chord([0, 4, 7]) # major triad a different way
        >>> c = Chord(['C', 'E', 'G']) # Cmaj
        >>> c = Chord(['G#', 'B', 'D#'], root='E') # rootless Emaj7

    Attributes:
        formula (list of Pitch): the intervals relative to the root.
        root (Pitch): the reference, defaults to first pitch.
        attrib (dict): dictionary of additional attributes

    '''
    def __init__(self, formula, root=None, attrib={}):
        if root:
            self._root = Pitch.make(root)
        else:
            self._root = Pitch.make(formula[0])
        self._formula = PitchSequence(formula)
        self.attrib = attrib
        self._update()

    def _update(self):
        self._pitches = [p + self._root for p in self._formula]

    @property
    def formula(self):
        return self._formula

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = Pitch.make(value)
        self._update()

    def __repr__(self):
        return f'Chord({self._notes}, {self.quality.__repr__()}, {self.root}, {self.attrib})'  