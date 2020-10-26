class Pattern:
    def __init__(self, tones, name=None):
        self.tones = tones
        self.name = name

    def __getitem__(self, i):
        return self.tones[i]

    def __len__(self):
        return len(self.tones)


class Voicing:
    def __init__(self, pattern, voicing, inversion):
        self.pattern = pattern
        self.voicing = voicing
        self.inversion = inversion

    def _update(self):
        self.tones = [self.pattern[(i+self.inversion)%len(self.pattern)] for i in self.voicing]
        for i in range(1, len(self.tones)):
            while self.tones[i] < self.tones[i-1]:
                self.tones[i] += 12
    def __getitem__(self, i):


def main():
    p = Pattern([0, 3, 7], 'Maj')
    print(len(p))
    print(p[2])

if __name__ == '__main__':
    main()