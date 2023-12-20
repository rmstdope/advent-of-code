import numpy as np
import copy
import math

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().strip().splitlines()

class Module:
    def __init__(self, prefix, name) -> None:
        self.prefix = prefix
        self.destinations = []
        self.pulses = []
        self.flip = False
        self.inputs = {}
        self.name = name

    def connect_from(self, source):
        self.inputs[source] = 0

    def connect_to(self, dest):
        self.destinations.append(dest)

    def queue(self, pulse, inp):
        self.pulses.append((pulse, inp))

    def handle(self):
        pulse, inp = self.pulses.pop(0)
        # print(inp, pulse, '->', self.name)
        if self.prefix == '&':
            self.inputs[inp] = pulse
        if self.prefix == '%':
            if pulse == 1:
                return 0, False
            else:
                self.flip = self.flip == False
                if self.flip:
                    return 1, True
                else:
                    return 0, True
        else:
            high = True
            for i in self.inputs:
                if self.inputs[i] == 0:
                    high = False
            if high:
                return 0, True
            else:
                return 1, True

broadcaster = []
modules = {}
for s in strs:
    s = s.split(' -> ')
    if s[0] == 'broadcaster':
        for c in s[1].split(', '):
            broadcaster.append(c)
    else:
        m = Module(s[0][0], s[0][1:])
        for d in s[1].split(', '):
            m.connect_to(d)
        modules[s[0][1:]] = m

for b in broadcaster:
    modules[b].connect_from('broadcaster')

for n,m in modules.items():
    for d in m.destinations:
        if d in modules:
            modules[d].connect_from(n)

handles = []
ones = 0
zeros = 0
presses = 0
xcp = 0
thp = 0
pdp = 0
bpp = 0
while xcp == 0 or thp == 0 or pdp == 0 or bpp == 0:
# for i in range(100000000):
    zeros += 1
    if presses % 1000000 == 0:
        print(presses, 'presses')
    presses += 1
    for b in broadcaster:
        modules[b].queue(0, 'broadcaster')
        zeros += 1
        handles.append(b)

    while handles:
        m = handles.pop(0)
        p, t = modules[m].handle()
        if m == 'xc' and p == 1 and xcp == 0:
            xcp = presses
            # print('xc: ', presses, 'presses')
        if m == 'th' and p == 1 and thp == 0:
            thp = presses
            # print('th: ', presses, 'presses')
        if m == 'pd' and p == 1 and pdp == 0:
            pdp = presses
            # print('pd: ', presses, 'presses')
        if m == 'bp' and p == 1 and bpp == 0:
            bpp = presses
            # print('bp: ', presses, 'presses')
        if t:
            for d in modules[m].destinations:
                if p == 1:
                    ones += 1
                else:
                    zeros += 1
                if d in modules:
                    modules[d].queue(p, m)
                    handles.append(d)
    if presses == 1000:
        part1 = ones * zeros

# &xc -> zh
# &th -> zh
# &pd -> zh
# &bp -> zh
# find the cycles of the above and the least common multiplier
part2 = math.lcm(xcp, thp, pdp, bpp)

print(f'{part1=}, {part2=}')
