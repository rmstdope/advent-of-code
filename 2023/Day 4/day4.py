import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

matching = []
part1 = 0
for s in strs:
    s = s.split(': ')[1]
    nums = s.split(' | ')
    my = nums[0].split(' ')
    my_numbers = []
    for x in my:
        if x != '':
            my_numbers.append(int(x))
    winning_numbers = []
    win = nums[1].split(' ')
    for x in win:
        if x != '':
            winning_numbers.append(int(x)) 
    num_right = 0
    for m in my_numbers:
        if m in winning_numbers:
            num_right += 1
    if num_right > 0:
        part1 += pow(2, num_right - 1)
    matching.append(num_right)

part2 = 0
copies = [ ]
for i in range(len(strs)):
    copies.append(1)
for i in range(len(strs)):
    for j in range(matching[i]):
        if i + j + 1 < len(strs):
            copies[i + j + 1] += copies[i]

part2 = sum(copies)
print(f'{part1=}, {part2=}')
