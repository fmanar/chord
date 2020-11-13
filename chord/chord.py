class Chord:
    '''A chord with fancy options.

    Attributes:
        formula (list of int): the chord tones relative to root.
        order (list of int): the ordering of the formula tones as formula 
            indexes. Defaults to the formula in order.
        octave (list of int): the relative octave to place the formula tones.
            Defaults to making the pitch sequence increasing.
        inversion (int): increment on the order array
        root (int): chord's root
    '''
    def __init__(self, formula, order=None, octave=None, inversion=0, root=0):
        self.formula = formula

        if order:
            self.order = order
        else:
            self.order = [i for i in range(len(self.formula))]

        if octave:
            self.octave = octave
        else:
            # build octaves the put each tone higher than last
            self.octave = []
            last = None
            for ord in self.order:
                curr = self.formula[ord]
                if last is None:
                    self.octave.append(0)
                elif last > curr:
                    self.octave.append(self.octave[-1] + 1)
                else:
                    self.octave.append(self.octave[-1])
                last = curr

        self.inversion = inversion
        self.root = root

    @property
    def pitches(self):
        pitches = []
        for ord, oct in zip(self.order, self.octave):
            index = ord + self.inversion
            pitches.append(
                self.root
                + self.formula[index % len(self.formula)] 
                + 12*(oct + index // len(self.formula))
            )
        return pitches