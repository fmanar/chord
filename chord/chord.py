class Chord:
    '''An ordered collection of pitches relative to a root.

    Can be either an absolute chord or a relative formula.

    Attributes:
        notes (list of Note): the notes that make up the chord.  Can also be a
            list of integers or note names and will be cast to Notes. 
        quality (str): description of chord type, e.g. Maj, min7b5 etc.
        root (Note): the reference Note, defaults to first note.

    '''
    def __init__(self, notes, quality='', root=None, attrib={}):
        self._notes = [Note.make(n) for n in notes]
        if root:
            self._root = Note.make(root)
        else:
            self._root = Note.make(notes[0])
        self.quality = quality
        self.attrib = attrib

    def __len__(self):
        return len(self._notes)

    @property
    def notes(self):
        return self._notes

    @property
    def root(self):
        return self._root

    def __getitem__(self, i):
        return self._notes[i] + self.root        

    def __iter__(self):
        return self._notes.__iter__()        

    def __str__(self):
        return self.root + self._notes.__str__()

    def __repr__(self):
        return f'Chord({self._notes}, {self.quality.__repr__()}, {self.root}, {self.attrib})'  