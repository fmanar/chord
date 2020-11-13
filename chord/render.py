def to_grid(pos, num_string=6):
    # │─└┘┬┴┌┐○●
    # sort the positions so we are guaranteed to encounter them in order
    pos.sort(key=lambda p: p[0])
    # s_min = pos[0][0]
    # s_max = pos[-1][0]
    s_min = 0
    s_max = s_min + num_string - 1
    pos.sort(key=lambda p: p[1])
    f_min = pos[0][1]
    f_max = pos[-1][1]

    header = '┌' + '┬'*(s_max - s_min - 1) + '┐'
    footer = '└' + '┴'*(s_max - s_min - 1) + '┘'
    
    print(header)
    i = 0
    for f in range(f_min, f_max+1):
        for s in range(s_min, s_max+1):
            if i < len(pos) and pos[i][1] == f and pos[i][0] == s:
                print('●', end='')
                i += 1
            else:
                print('│', end='')
        print('')
    print(footer)

def to_tab(pos, num_string=6):
    pos.sort(key=lambda p: p[0])
    i = 0
    for s in range(num_string):
        if i < len(pos) and pos[i][0] == s:
            print(pos[i][1], end='')
            i += 1
        else:
            print('-', end='')
    print('')