def to_text(pos):
    low_fret = 128
    high_fret = 0
    low_string = 128
    high_string = 0
    for p in pos:
        if p.fret < low_fret:
            low_fret = p.fret
        if p.fret > high_fret:
            high_fret = p.fret
        if p.string < low_string:
            low_string = p.string
        if p.string > high_string:
            high_string = p.string
    # │─└┘┬┴┌┐○●
    # print the frets
    char_reg = '●'
    char_root = '○'
    header = '┌' + '┬'*(high_string - low_string - 1) + '┐'
    footer = '└' + '┴'*(high_string - low_string - 1) + '┘'

    # sort the positions so we are guaranteed to encounter them in order
    pos.sort(key=lambda p: p.string)
    pos.sort(key=lambda p: p.fret)
    
    print(header)
    i = 0
    for f in range(low_fret, high_fret+1):
        for s in range(low_string, high_string+1):
            if i < len(pos) and pos[i].fret == f and pos[i].string == s:
                print(char_reg, end='')
                i += 1
            else:
                print('│', end='')
        print('')
    print(footer)