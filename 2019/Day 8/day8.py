import numpy as np
import copy
from textwrap import wrap

f = open('prod.txt')
strs = f.read().splitlines()[0]

layer_size = 25 * 6
layers = wrap(strs, layer_size)

best = -1
num_best_0 = layer_size
num_best_1 = layer_size
num_best_2 = layer_size
for i,l in enumerate(layers):
    zeros = l.count("0")
    if (zeros < num_best_0):
        num_best_0 = zeros
        num_best_1 = l.count("1")
        num_best_2 = l.count("2")
        best = i

part1 = num_best_1 * num_best_2

print(f'{part1=}')

i = 0
for y in range(6):
    for x in range(25):
        l = 0
        while (layers[l][i] == '2'):
            l += 1
        if (layers[l][i] == '1'):
            print("*", end="")
        else:
            print(" ", end="")
        i += 1
    print('')

