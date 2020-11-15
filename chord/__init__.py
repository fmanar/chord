from .chord import Chord
from .pitch import pitchify, depitchify
from .render import to_grid, to_tab
from .render_cairo import to_cairo

def play(pitches, strings, tunings):
    return [(s, p - tunings[s]) for p, s in zip(pitches, strings)]