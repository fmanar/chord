import functools
import re

@functools.total_ordering
class Pitch:
    '''Stores a single pitch.

    Pitch is represented as an integer number of half-steps above a
    reference. Support is provided to name the pitches by a letter, a sharp
    (#) or flat (b) and an optional octave number (corresponds to the MIDI
    tuning standard with C4=60). As a string, this would be something like
    'F#4'. Support for addition and subtraction is provided, and works with
    integers. Attributes are erased if two pitches have disimilar
    dictionaries.

    Attributes:
        pitch (int): the pitch
        attrib (dict): dictionary of additional attributes

    Examples:
        >>> p = Pitch(60) # a middle C
        >>> p = Pitch('C4') # also a middle C

    '''
    def __init__(self, value, attrib={}):
        if isinstance(value, int):
            self.pitch = value
        elif isinstance(value, str):
            self.pitch = 0
            self.set_name(value)
        else:
            raise ValueError
        self.attrib = attrib

    @classmethod
    def make(cls, value):
        '''A factory method to allow easy casting.'''
        if isinstance(value, cls):
            return value
        else:
            return Pitch(value)

    def get_octave(self):
        '''Return MIDI octave number.'''
        return (self.pitch // 12) - 1

    def get_class(self):
        '''Return pitch modulo 12'''
        return self.pitch % 12

    def get_name(self, absolute=False, flats=False):
        '''Return letter name for pitch.'''
        names_sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 
                'F#', 'G', 'G#', 'A', 'A#', 'B']
        names_flat  = ['C', 'Db', 'D', 'Eb', 'E', 'F', 
                'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        octave = self.get_octave()
        pitch = self.get_class()

        if flats:
            name = names_flat[pitch]
        else:
            name = names_sharp[pitch]

        if absolute:
            name += f'{octave}'

        return name

    def set_name(self, name):
        '''Deduce pitch from letter name.'''
        d = {'c':0, 'c#':1, 'db':1, 'd':2, 'd#':3, 'eb':3, 
                'e':4, 'f':5, 'f#':6, 'gb':6, 'g':7, 'g#':8, 
                'ab':8, 'a':9, 'a#':10, 'bb':10, 'b':11,
        }
        match = re.match('([a-zA-Z][#b]?)(\d*)', name)
        if match:
            name = match.group(1).lower()
            try:
                octave = int(match.group(2).lower())
            except:
                octave = -1
            self.pitch = d[name] + 12*(octave + 1)
        else:
            raise ValueError

    def __str__(self):
        return f'{self.pitch}'
    
    def __repr__(self):
        return f'Pitch({self.pitch}, {self.attrib})'

    def __eq__(self, other):
        if not isinstance(other, Pitch):
            other = Pitch(other)
        return self.pitch == other.pitch

    def __lt__(self, other):
        if not isinstance(other, Pitch):
            other = Pitch(other)
        return self.pitch < other.pitch

    def __add__(self, other):
        if isinstance(other, Pitch):
            return Pitch(self.pitch + other.pitch)
        elif isinstance(other, int):
            return Pitch(self.pitch + other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Pitch):
            return Pitch(self.pitch - other.pitch)
        elif isinstance(other, int):
            return Pitch(self.pitch - other)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return Pitch.make(other) - self

    def __iadd__(self, other):
        if isinstance(other, Pitch):
            self.pitch += other.pitch
            return self
        elif isinstance(other, int):
            self.pitch += other
            return self
        else:
            return NotImplemented
        
    def __isub__(self, other):
        if isinstance(other, Pitch):
            self.pitch -= other.pitch
            return self
        elif isinstance(other, int):
            self.pitch -= other
            return self
        else:
            return NotImplemented