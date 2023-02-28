import numpy as np
import copy

f = open('input.txt')
strs = f.read().splitlines()
start = list(map(int, strs[0].split(',')))

def run(n):
    numbers = {}
    for t, s in enumerate(start):
        numbers[s] = t + 1
    next = 0
    for t in range(len(start) + 1, n):
        oldt = numbers.get(next)
        numbers[next] = t
        if oldt == None:
            next = 0
        else:
            next = t - oldt
    return next


part1 = run(2020)
part2 = run(30000000)
print(f'{part1=}, {part2=}')
