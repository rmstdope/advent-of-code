import numpy as np
import copy
from collections import defaultdict

# f = open('test.txt')
f = open('prod.txt')
strs = f.read().strip().splitlines()
map = [[c for c in s] for s in strs]

maxx = len(map[0])
maxy = len(map)

for y in range(maxy):
    for x in range(maxx):
        if map[y][x] == 'S':
            startx = x
            starty = y
            map[y][x] = '.'

def traverse(num_steps):
    plots = {(startx, starty)}
    num_plots = defaultdict(int)
    for i in range(num_steps):
        new_plots = set()
        for plot in plots:
            x, y = plot
            for n in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newx = x + n[0]
                newy = y + n[1]
                if map[newy % maxx][newx % maxy] != "#":
                    new_plots.add((newx, newy))
        plots = new_plots
        num_plots[i + 1] += len(new_plots)
    return num_plots

plots = traverse(2 * maxx + startx)
part1 = plots[64]

x = 26501365
x0 = startx
x1 = maxx + startx
x2 = 2 * maxx + startx
y0 = plots[x0]
y1 = plots[x1]
y2 = plots[x2]
l0 = ((x - x1) * (x - x2)) // ((x0 - x1) * (x0 - x2))
l1 = ((x - x0) * (x - x2)) // ((x1 - x0) * (x1 - x2))
l2 = ((x - x0) * (x - x1)) // ((x2 - x0) * (x2 - x1))
part2 = y0 * l0 + y1 * l1 + y2 * l2

print(f'{part1=}, {part2=}')
