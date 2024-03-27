import numpy as np
import copy
from collections import defaultdict
import networkx as nx
import sympy
import heapq
import sys
import math

f = open('test.txt')
#f = open('prod.txt')
strs = f.read().strip().splitlines()

part1 = 0
part2 = 0

print(f'{part1=}, {part2=}')
