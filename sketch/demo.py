import func

# the chord tones and strings to play them on
# chord = [0, 4, 7, 11]
# voicing = [0, 2, 3, 1]
# strings = [1, 2, 3, 4]
# inversion = 3

chord = [0, 3, 7]
voicing = [0, 2, 0, 1, 2, 0]
strings = [0, 1, 2, 3, 4, 5]
inversion = 0

# list of string tuning
tuning = [7, 12, 17, 22, 27, 32] # p4
# tuning = [7, 12, 17, 22, 26, 31] # standard

print(f'chord:   {chord}')
print(f'voicing: {voicing}')
print(f'strings: {strings}')
print(f'inv:     {inversion}')

func.display_chord(chord, voicing, strings, inversion, tuning)