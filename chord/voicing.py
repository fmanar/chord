class Voicing:
    '''An array-like set of tones decribing a chord voicing.

    Uses parallel arrays.  Pythonic?
    '''
    def __init__(self, formula, order=None, octave=None, inversion=0, root=0):
        self.formula = formula
        if order:
            self.order = order
        else:
            self.order = [i for i in range(len(formula))]
            
        if octave:
            self.octave = octave
        else:
            self.octave = [0 for _ in self.order]
            # build octaves the put each tone higher than last
            for i in range(1, len(self.order)):
                self.octave[i] = self.octave[i-1]
                if ((self.formula[self.order[i-1]] + 12*self.octave[i-1]) 
                        > (self.formula[self.order[i]] + 12*self.octave[i])):
                    self.octave[i] += 1

        self.inversion = inversion
        self.root = root
        self.notes = [0 for _ in self.order]
        self._update()

    def _update(self):
        for i in range(len(self.order)):
            formula_index = (self.order[i] + self.inversion) % len(self.formula)
            self.notes[i] = self.root + self.formula[formula_index] + 12*self.octave[i]

    def __len__(self):
        return len(self.notes)

    def __getitem__(self, i):
        return self.notes[i]        

    def __iter__(self):
        return self.notes.__iter__()        

    def __str__(self):
        return self.notes.__str__()  