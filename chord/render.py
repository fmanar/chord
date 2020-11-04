def to_text(pos):
    # │─└┘┬┴┌┐○●
    # sort the positions so we are guaranteed to encounter them in order
    pos.sort(key=lambda p: p.string)
    s_min = pos[0].string
    s_max = pos[-1].string
    pos.sort(key=lambda p: p.fret)
    f_min = pos[0].fret
    f_max = pos[-1].fret

    header = '┌' + '┬'*(s_max - s_min - 1) + '┐'
    footer = '└' + '┴'*(s_max - s_min - 1) + '┘'
    
    print(header)
    i = 0
    for f in range(f_min, f_max+1):
        for s in range(s_min, s_max+1):
            if i < len(pos) and pos[i].fret == f and pos[i].string == s:
                print('●', end='')
                i += 1
            else:
                print('│', end='')
        print('')
    print(footer)