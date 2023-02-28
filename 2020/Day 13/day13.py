import numpy as np
import copy

f = open('input.txt')
strs = f.read().splitlines()
part1 = 0
part2 = 0
arrival = int(strs[0])
buses = []
for b in strs[1].split(','):
    if b != 'x':
        buses.append(int(b))

id = -1
best = 100000
for b in buses:
    time = 0
    while time < arrival:
        time += b
    if time - arrival < best:
        best = time - arrival
        id = b

# part 2


class poly:
    def __init__(self, mul, const):
        self.mul = mul
        self.const = const


class layer:
    def __init__(self, str):
        self.polys = []
        for i, s in enumerate(str.split(',')):
            if s != 'x':
                self.polys.append(poly(int(s), -i))

    def resolve(self):
        self.next = layer('x')
        if len(self.polys) != 2:
            for p in self.polys[1:]:
                p.const -= self.polys[0].const
                n = 1
                while (self.polys[0].mul * n - p.const) % p.mul != 0:
                    n += 1
                # Result is nx = p.mul * x + n
                self.next.polys.append(poly(p.mul, n))
            x = self.next.resolve()
            return self.polys[0].mul * x + self.polys[0].const
        else:
            found = False
            x1 = 0
            while not found:
                x1 += 1
                if (x1 * self.polys[0].mul + self.polys[0].const - self.polys[1].const) % self.polys[1].mul == 0:
                    found = True
            return x1 * self.polys[0].mul + self.polys[0].const


# strs[1] = '17,x,13,19'
# x = 17 * n1 - 0
# x = 13 * n2 - 2
# x = 19 * n3 - 3
# n2 = (17 * n1 + 2 - 0) / 13
# n3 = (17 * n1 + 3 - 0) / 19
# n1 = 6+13*x1
# n1 = 11+19*x2


part1 = id * best
l = layer(strs[1])
part2 = l.resolve()

print(f'{part1=}, {part2=}')
