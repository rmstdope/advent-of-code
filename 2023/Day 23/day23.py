import numpy as np
import copy
import heapq
import sys
from collections import defaultdict 

f = open('test.txt')
#f = open('prod.txt')
strs = f.read().strip().splitlines()
startx = 1
starty = 0
endx = strs[len(strs) - 1].find('.')
endy = len(strs) - 1
part1 = 0
part2 = 0


map = [[c for c in s] for s in strs]
maxx = len(map[0])
maxy = len(map)

# Find nav point
navpoints = [(startx, starty)]
for y in range(maxy):
    for x in range(maxx):
        num_choices = 0
        if map[y][x] == '#':
            continue
        for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newx = x + n[0]
            newy = y + n[1]
            if 0 <= newx < maxx and 0 <= newy < maxy and map[newy][newx] != '#':
                num_choices += 1
        if num_choices > 2:
            navpoints.append((x, y))
navpoints.append((endx, endy))

graph = {}
def buildgraph(p2):
    global graph
    graph = {}
    for p in navpoints:
        q = [(p[0], p[1], 0)]
        visited = {}
        graph[(p[0], p[1])] = []
        while q:
            x, y, c = heapq.heappop(q)
            if (x, y) in visited:
                continue
            visited[(x, y)] = True
            if (x != p[0] or y != p[1]) and (x, y) in navpoints:
                graph[(p[0], p[1])].append((x, y, c))
                continue
            for n in [(-1, 0, '<'), (1, 0, '>'), (0, -1, '^'), (0, 1, 'v')]:
                newx = x + n[0]
                newy = y + n[1]
                if 0 <= newx < maxx and 0 <= newy < maxy and map[newy][newx] != '#':
                    if not p2 and map[newy][newx] in ['<', '^', '>', 'v'] and map[newy][newx] != n[2]:
                        continue
                    heapq.heappush(q, (newx, newy, c + 1))

visited = defaultdict(lambda:False)
def dfs(x, y, cost, p2):
    global part1
    global part2
    if visited[(x, y)]:
        return
    visited[(x, y)] = True
    if x == endx and y == endy and p2:
        part2 = max(part2, cost)
    if x == endx and y == endy and not p2:
        part1 = max(part1, cost)
    for (newx, newy, addcost) in graph[(x, y)]:
        dfs(newx, newy, cost + addcost, p2)
    visited[(x, y)] = False

buildgraph(False)
dfs(startx, starty, 0, False)

buildgraph(True)
dfs(startx, starty, 0, True)

print(f'{part1=}, {part2=}')
