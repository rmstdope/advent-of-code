import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

orbits = dict()
orbits_rev = dict()
for s in strs:
    nodes = s.split(')')
    orbits_rev[nodes[1]] = nodes[0]
    if nodes[0] not in orbits:
        orbits[nodes[0]] = [ nodes[1] ]
    else:
        orbits[nodes[0]].append(nodes[1])

#for k,v in orbits.items():

def get_orbits(node, num_orbits):
    new_num_orbits = num_orbits
    if node not in orbits:
        return num_orbits
    for o in orbits[node]:
        new_num_orbits += get_orbits(o, num_orbits + 1)
    return new_num_orbits

part1 = get_orbits("COM", 0)

def get_path(start):
    if start not in orbits_rev:
        return [start]
    return get_path(orbits_rev[start]) + [start]

path1 = get_path('YOU')
path2 = get_path('SAN')

while path1[0] == path2[0]:
    path1.pop(0)
    path2.pop(0)

part2 = len(path1) + len(path2) - 2

print(f'{part1=}, {part2=}')
