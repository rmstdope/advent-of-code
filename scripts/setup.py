import sys
import os
import urllib.request
# from aocd import get_data, AocdError

if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} [year] [day]')
    exit(code=1)

year = sys.argv[1]
day = sys.argv[2]

if int(year) < 2015 or int(year) > 2030:
    print(f'[year] must be [2015..2030]')
    exit(code=1)

if int(day) < 1 or int(day) > 25:
    print(f'[day] must be [1..25]')
    exit(code=1)

# Assume Windows/Linux/MacOS compatible path separators
if os.name == 'nt':
    separator = '\\'
else:
    separator = '/'
print('Scanning path')
dirs = os.getcwd().split(separator)
dir_index = -1
base_dir = ''
build_dir = ''
for i,d in enumerate(dirs):
    build_dir += d + separator
    if d == 'advent-of-code':
        base_dir += build_dir
        dir_index = i

if dir_index == -1:
    print(f'Could not find advent-of-code parent directory')
    exit(code=1)

print('Base path found')
year_dir = base_dir + year + separator

if not os.path.exists(year_dir):
    os.makedirs(year_dir)
    print(f'Created year directory ({year})')
else:
    print(f'Year directory found ({year})')
    

# day_dir = year_dir + 'Day ' + day + '\\'

# if not os.path.exists(day_dir):
#     os.makedirs(day_dir)
#     print(f'Created day directory (Day {day})')
# else:
#     print(f'Day directory found (Day {day})')

filename = year_dir + 'day' + day + '.py'
if not os.path.exists(filename):
    open(filename, 'w').write('''import os
import numpy as np
import copy
import collections
import networkx as nx
import sympy
import heapq
import sys
import math
import itertools
from functools import cache
from z3 import *
from aoctools import *
from BaseSolver import BaseSolver
from aocd.models import Example

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

#     def get_examples(self):
#         examples = []
#         examples.append(Example(input_data=\'\'\'
#\'\'\', answer_a='', answer_b=None))
#         return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
#solver.solve_examples_2()
#solver.solve_problem_2()
''')
    print(f'Boilerplate code created')
else:
    print(f'Boilerplate code already exists')

# filename = day_dir + 'test.txt'
# if not os.path.exists(filename):
#     open(filename, 'w').write('')
#     print(f'Test file created')
# else:
#     print(f'Test file already exists')

# filename = day_dir + 'prod.txt'
# if not os.path.exists(filename):
#     try:
#         data = get_data(day=int(day), year=int(year))
#         open(filename, 'w').write(data)
#         print(f'Prod file created')
#     except AocdError as e:
#         print(f'Error downloading production file: {e}')
#         exit(code=1)
# else:
#     print(f'Production file already exists')

#os.chdir(day_dir)
