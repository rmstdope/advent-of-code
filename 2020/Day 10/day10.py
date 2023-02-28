import numpy as np

f = open('input.txt')
str = list(map(int, f.read().splitlines()))
str.append(0)
str.append(max(str) + 3)

part1 = 0
part2 = 0

str = sorted(str)
ones = 0
threes = 0
for j1, j2 in zip(str, str[1:]):
    if abs(j1 - j2) == 1:
        ones += 1
    if abs(j1 - j2) == 3:
        threes += 1
part1 = ones * threes

numparts = np.zeros(len(str), dtype=np.int64)
numparts[0] = 1
for i1, j in enumerate(str):
    for i2 in range(i1):
        if str[i1] - str[i2] <= 3:
            numparts[i1] += numparts[i2]

part2 = numparts[len(str) - 1]

print(f'{part1=}, {part2=}')
