class Instrument:
    '''A description of strings and tunings.

    '''
    def __init__(self, tuning):
        self.tuning = tuning

    def play(self, note, string):
        '''Put note on the fretboard.
        
        Args:
            note (Pitch): the note to fret.
            string (int): the string to play it on.

        Returns:
            (Pos): the resulting positions

        '''
        return Pos(string, int(note) - self.tuning[string])

class Pos:
    def __init__(self, string, fret):
        self.string = string
        self.fret = fret

    def __str__(self):
        return f'{self.string}/{self.fret}'