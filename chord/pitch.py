import re

def pitchify(pitch):
    '''Translate letter pitches into numbers.

    Pitch is represented as an integer number of half-steps above C. A name
    is a letter A-G, a sharp (#) or flat (b) and an optional octave number
    (where 'C4' = 60). For example 'F#' = 6.

    Input can be single pitch or a list which will be returned in kind, or 
    separate inputs to be returned as a list.

    '''
    if isinstance(pitch, list) or isinstance(pitch, tuple):
        return [_from_letter(p) for p in pitch]
    else:
        return _from_letter(pitch)

def depitchify(pitch, absolute=False, flats=False):
    '''Translate number pitches into letters.'''
    if isinstance(pitch, list) or isinstance(pitch, tuple):
        return [_to_letter(p, absolute, flats) for p in pitch]
    else:
        return _to_letter(pitch, absolute, flats)

def _to_letter(pitch, absolute, flats):
    '''Turn pitch into letter name.'''
    names_sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 
            'F#', 'G', 'G#', 'A', 'A#', 'B']
    names_flat  = ['C', 'Db', 'D', 'Eb', 'E', 'F', 
            'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
    octave = pitch // 12
    pc = pitch % 12
    if flats:
        name = names_flat[pc]
    else:
        name = names_sharp[pc]
    if absolute:
        name += f'{octave}'
    return name

def _from_letter(name):
    '''Deduce pitch from letter name.'''
    d = {'c':0, 'c#':1, 'db':1, 'd':2, 'd#':3, 'eb':3, 
            'e':4, 'f':5, 'f#':6, 'gb':6, 'g':7, 'g#':8, 
            'ab':8, 'a':9, 'a#':10, 'bb':10, 'b':11,
    }
    match = re.match('([a-zA-Z][#b]?)([+-]?\d*)', name)
    if match:
        name = match.group(1).lower()
        try:
            octave = int(match.group(2).lower())
        except:
            octave = 0
        return d[name] + 12*octave
    else:
        raise ValueError('Could not translate pitch')


def main():
    data = ['C#5', 'F5', 'Ab5']
    # data = 'Eb'
    p = pitchify(data)
    s = depitchify(p, absolute=True)
    print(data, p, s)

if __name__ == '__main__':
    main()