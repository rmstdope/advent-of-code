import numpy as np
import copy

f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()
active = set()
for y, str in enumerate(strs):
    for x, c in enumerate(str):
        if c == '#':
            active.add((x, y))


part1 = 0
part2 = 0

print(f'{part1=}, {part2=}')
