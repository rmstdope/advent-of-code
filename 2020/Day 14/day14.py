import numpy as np
import copy

f = open('input.txt')
strs = f.read().splitlines()
part1 = 0
part2 = 0


memory = {}
allbits = int('0b111111111111111111111111111111111111', 2)
for s in strs:
    inst = s.split(' ')
    if inst[0] == 'mask':
        mask = inst[2]
    else:
        addr = inst[0][4:len(inst[0]) - 1]
        data = int(inst[2])
        for i, c in enumerate(mask):
            m = 2**(35 - i)
            if c == '1':
                data |= m
            elif c == '0':
                data &= (m ^ allbits)
        memory[addr] = data

part1 = 0
for addr, data in memory.items():
    part1 += data

memory = {}
for s in strs:
    inst = s.split(' ')
    if inst[0] == 'mask':
        mask = inst[2]
    else:
        addr = int(inst[0][4:len(inst[0]) - 1])
        data = int(inst[2])
        numx = mask.count('X')
        for x in range(2**numx):
            xpos = 0
            for i, c in enumerate(mask):
                if c == '0':
                    pass
                elif c == '1':
                    m = 2**(35 - i)
                    addr |= m
                elif c == 'X':
                    # clear bit
                    m = 2**(35 - i)
                    addr &= (m ^ allbits)
                    # insert correct bit
                    addr |= ((x >> xpos) & 1) << (35 - i)
                    xpos += 1

            memory[addr] = data

part2 = 0
for addr, data in memory.items():
    part2 += data


print(f'{part1=}, {part2=}')
