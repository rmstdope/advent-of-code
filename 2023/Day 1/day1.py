import numpy as np
import copy
import re

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

def get_number(s, i, text):
    numbers = ['<>', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if s[i] <= '9' and s[i] >= '0':
        return s[i]
    for i2,n in enumerate(numbers):
        if text and s[i:i +  len(n)] == n:
            return str(i2)
    return ''

def get_cal_values(strs, text):
    val = 0
    for s in strs:
        num = ''
        for i in range(len(s)):
            num += get_number(s, i, text)
            if len(num) == 1:
                break
        for i in reversed(range(len(s))):
            num += get_number(s, i, text)
            if len(num) == 2:
                break
        #print(num)
        val += int(num)
    return val

part1 = get_cal_values(strs, False)
part2 = get_cal_values(strs, True)

print(f'{part1=}, {part2=}')
