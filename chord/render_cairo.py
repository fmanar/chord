# lets draw some stuff with ciaro!
from math import pi

import cairo

def to_cairo(pos, num_strings=6):
    width, height = 300, 400
    w, h = 0.6, 0.8*height/width

    surface = cairo.ImageSurface(cairo.Format.ARGB32, width, height)
    cr = cairo.Context(surface)
    cr.translate(width/2, height/2)
    cr.scale(width, width)
    cr.set_source_rgba(1.0, 1.0, 1.0, 1.0)

    # fill bg
    cr.paint()
    cr.set_source_rgba(0.0, 0.0, 0.0, 1.0)

    # draw strings
    n = num_strings - 1
    string = [-w/2 + w/n*i for i in range(num_strings)]
    for x in string:
        cr.move_to(x, +h/2)
        cr.line_to(x, -h/2)

    # draw frets
    n = 5
    fret = []
    for i in range(n + 1):
        cr.move_to(-w/2, +h/2 - h/n*i)
        cr.line_to(+w/2, +h/2 - h/n*i)
        fret.append(-h/2 + h/n*(i - 0.5))

    cr.set_line_width(0.01)
    cr.set_line_cap(cairo.LineCap.SQUARE)
    cr.stroke()

    # draw positions
    r = 0.05
    for p in pos:
        x = string[p[0]]
        y = fret[p[1]]
        cr.arc(x, y, r, 0.0, 2.0*pi)
        cr.fill()

    surface.write_to_png('pic.png')

def main():
    pos = [(0, 1), (1, 2), (3, 4)]
    to_cairo(pos)

if __name__ == '__main__':
    main()
