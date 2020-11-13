class Instrument:
    '''A description of strings and tunings.

    Attributes:
        tuning (list of int): the tuning of each string

    '''
    def __init__(self, tuning):
        self.tuning = tuning

    def get_num_strings(self):
        return len(tuning)

    def play(self, pitch, string):
        '''Put note on the fretboard.
        
        Args:
            pitch (int): the pitch to fret.
            string (int): the string to play it on.

        Returns:
            (2-tuple of int): the resulting position

        '''
        return (string, pitch - self.tuning[string])