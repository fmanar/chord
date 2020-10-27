class Instrument:
    '''A description of strings and tunings.

    '''
    def __init__(self, tuning):
        self.tuning = tuning

    def play(self, notes, strings):
        '''Put notes on the fretboard.
        
        Args:
            notes (list of int): the set of notes to fret
            strings (list of int): a parallel array of strings to play them on.

        Returns:
            (list of Pos): the resulting positions

        '''
        pos = []
        for n, s in zip(notes, strings):
            pos.append(Pos(s, n - self.tuning[s]))
        return pos

class Pos:
    def __init__(self, string, fret):
        self.string = string
        self.fret = fret

    def __str__(self):
        return f'{self.string}/{self.fret}'