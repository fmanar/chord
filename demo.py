import chord as c

crd = c.Chord(
    formula=[0, 4, 7],
    order=[0, 1, 2, 0, 2, 0],
    inversion=0,
    root=c.pitchify('G2'),
    )
pos = c.play(
    pitches=crd.pitches,
    strings=[0, 1, 2, 3, 4, 5],
    tunings=c.pitchify(['E2', 'A2', 'D3', 'G3', 'B3', 'E4']),
    )
print(f'Formula   {crd.formula}')
print(f'Order     {crd.order}')
print(f'Octave    {crd.octave}')
print(f'Inversion {crd.inversion}')
print(f'Root      {crd.root} ({c.depitchify(crd.root)})')
print(f'Pitches   {crd.pitches} ({c.depitchify(crd.pitches)})')
print(f'Positions {pos}')
c.to_tab(pos)
c.to_grid(pos)
c.to_cairo(pos)