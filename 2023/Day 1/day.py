import numpy as np
import copy
import re

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

part1 = 0
numbers = ['<>', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for s in strs:
    num = ''
    for i in range(len(s)):
        if s[i] <= '9' and s[i] >= '0':
            num += s[i]
            break
        found = False
        for i2,n in enumerate(numbers):
            if s[i:i +  len(n)] == n:
                num += str(i2)
                print(n)
                found = True
        if found:
            break
    for i in reversed(range(len(s))):
        if s[i] <= '9' and s[i] >= '0':
            num += s[i]
            break
        found = False
        for i2,n in enumerate(numbers):
            if s[i:i + len(n)] == n:
                num += str(i2)
                print(n)
                found = True
        if found:
            break
    print(num)
    part1 += int(num)
part2 = 0

print(f'{part1=}, {part2=}')
