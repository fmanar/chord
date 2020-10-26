def voice(chord, voicing, inversion):
    tones = [chord[(i+inversion)%len(chord)] for i in voicing]
    for i in range(1, len(tones)):
        while tones[i] < tones[i-1]:
            tones[i] += 12
    return tones

def fret(tones, strings, tuning):
    frets = [-1 for _ in tuning]
    roots = [False for _ in tuning]
    low = 0
    for s, t in zip(strings, tones):
        frets[s] = t - tones[0] - tuning[s]
        if frets[s] < low:
            low = frets[s]
        if t%12 == 0:
            roots[s] = True

    # shift chord into positive
    for s in strings:
        frets[s] -= low
    return frets, roots

def render(frets, roots):
    low = 128
    high = 0
    for f in frets:
        if 0 <= f < low:
            low = f
        if 0 <= f > high:
            high = f
    # │─└┘┬┴┌┐○●◙
    # print the frets
    char_reg = '●'
    char_root = '○'
    print('┌┬┬┬┬┐')
    for f in range(low, high+1):
        for s in range(len(frets)):
            if frets[s] == f and roots[s]:
                print(char_root, end='')
            elif frets[s] == f:
                print(char_reg, end='')
            else:
                print('│', end='')
        print('')
    print('└┴┴┴┴┘')

def display_chord(chord, voicing, strings, inversion, tuning):
    tones = voice(chord, voicing, inversion)
    frets, roots = fret(tones, strings, tuning)
    render(frets, roots)