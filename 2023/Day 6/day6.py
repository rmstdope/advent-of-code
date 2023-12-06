import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

times = []
for s in strs[0].split(' ')[1:]:
    if s != '':
        times.append(int(s))
dist = []
for s in strs[1].split(' ')[1:]:
    if s != '':
        dist.append(int(s))

def find_ways():
    global times
    global dist
    result = 1
    for i in range(len(times)):
        wins = 0
        for t in range(times[i]):
            this_dist = t * (times[i] - t)
            if this_dist > dist[i]:
                wins += 1
        result *= wins
    return result

part1 = find_ways()
times = [int(strs[0][11:].replace(' ', ''))]
dist = [int(strs[1][11:].replace(' ', ''))]
part2 = find_ways()

print(f'{part1=}, {part2=}')
