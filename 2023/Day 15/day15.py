import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().strip()

def get_hash(s):
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    return value

boxes = []
for i in range(256):
    boxes.append([])

part1 = 0
for s in strs.split(','):
    part1 += get_hash(s)

def remove_label(box, label):
    newboxes = []
    for l in boxes[box]:
        if l[:len(label) + 1] != label + ' ':
            newboxes.append(l)
    boxes[box] = newboxes

def replace_label(box, label, num):
    for i,l in enumerate(boxes[box]):
        if l[:len(label) + 1] == label + ' ':
            boxes[box][i] = label + ' ' + num
            return True
    return False

for s in strs.split(','):
    if s.find('=') != -1:
        num = s.split('=')[1]
        label = s.split('=')[0]
        box = get_hash(label)
        if not replace_label(box, label, num):
            boxes[box].append(label + ' ' + num)
    else:
        label = s.split('-')[0]
        box = get_hash(label)
        remove_label(box, label)

part2 = 0
for i,b in enumerate(boxes):
    for i2,s in enumerate(b):
        part2 += (1 + i) * (i2 + 1) * int(s.split(' ')[1])

print(f'{part1=}, {part2=}')
