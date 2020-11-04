from chord.pitch import Pitch

class Chord:
    '''An ordered collection of pitches relative to a root.

    Can be either an absolute chord or a relative formula. The pitches are
    assumed to be monotonically increasing, though this isn't enforced.

    Examples:
        >>> c = Chord([Pitch(0), Pitch(4), Pitch(7)]) # major triad
        >>> c = Chord([0, 4, 7]) # major triad a different way
        >>> c = Chord(['C', 'E', 'G']) # Cmaj
        >>> c = Chord(['G#', 'B', 'D#'], root='E') # rootless Emaj7

    Attributes:
        pitches (list of Pitch): the notes that make up the chord shifted by
            the root.
        formula (list of Pitch): the intervals relative to the root.
        root (Pitch): the reference, defaults to first pitch.
        attrib (dict): dictionary of additional attributes

    '''
    def __init__(self, pitches, root=None, attrib={}):
        if root:
            self.root = Pitch.make(root)
        else:
            self.root = Pitch.make(pitches[0])
        self.formula = [Pitch.make(p) - self.root for p in pitches]
        self.attrib = attrib

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