import numpy as np
import copy
from collections import defaultdict
import networkx as nx

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().strip().splitlines()

conns = defaultdict(set)
conn = {}
for s in strs:
    s = s.split(': ')
    for c in s[1].split(' '):
        conns[s[0]].add(c)
        conns[c].add(s[0])

graph = nx.DiGraph()
for key, values in conns.items():
    for value in values:
        graph.add_edge(key, value, capacity = 1)

first = list(conns.keys())[0]
part1 = 0
for y in conns.keys():
    if first != y:
        cut_value, partition = nx.minimum_cut(graph, first, y)
        if cut_value == 3:
            part1 = len(partition[0]) * len(partition[1])
            break

print(f'{part1=}')



