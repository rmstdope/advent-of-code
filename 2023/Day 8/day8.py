import numpy as np
import copy
import math

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()
instructions = strs[0]

nodes = {}
for s in strs[2:]:
    nodes[s[0:3]] = [s[7:10], s[12:15]]

i = 0
part1 = 0
cur_node = 'AAA'
while cur_node != 'ZZZ':
    ins = instructions[i]
    if ins == 'L':
        cur_node = nodes[cur_node][0]
    else:
        cur_node = nodes[cur_node][1]
    i += 1
    part1 += 1
    if i == len(instructions):
        i = 0

def find_loop(node):
    i = 0
    num = 0
    while True:
        ins = instructions[i]
        if ins == 'L':
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        i += 1
        num += 1
        if i == len(instructions):
            i = 0
        if node[2] == 'Z':
                return num

loops = []
for n in nodes:
    if n[2] == 'A':
        loops.append(find_loop(n))

part2 = 1
for v in loops:
    part2 = math.lcm(part2, v)

print(f'{part1=}, {part2=}')
