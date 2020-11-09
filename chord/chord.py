from .pitch import Pitch

class Chord:
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
        pitches (list of Pitch): the absolute pitches that make up the chord.  
            The formula shifted by the root.
        formula (list of Pitch): the intervals relative to the root.
        root (Pitch): the reference, defaults to first pitch.
        attrib (dict): dictionary of additional attributes

    '''
    def __init__(self, pitches=None, formula=None, root=None, attrib={}):
        if root:
            self.root = Pitch.make(root)
        else:
            self.root = Pitch.make(pitches[0])
        self.formula = [Pitch.make(p) - self.root for p in pitches]
        self.attrib = attrib

    @classmethod
    def make(cls, value):
        '''A factory method to allow easy casting.'''
        if isinstance(value, cls):
            return value
        else:
            return Chord(value)


    def __len__(self):
        return len(self.formula)

    @property
    def pitches(self):
        return [p + self.root for p in self.formula]

    def __str__(self):
        tmp = []
        for p in self.pitches:
            tmp.append(str(p))
        return '[' + ', '.join(tmp) + ']'

    def __repr__(self):
        return f'Chord({self._notes}, {self.quality.__repr__()}, {self.root}, {self.attrib})'  