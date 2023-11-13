import numpy as np
import copy

#f = open('test.txt')
#f = open('prod.txt')
#str = f.read().splitlines()

part1 = 0
part2 = 0

start = 264793
end = 803935

#digits = [0, 0, 0, 0, 0, 0]

def check_password(i1, i2, i3, i4, i5, i6):
    val = i1 * 100000 + i2 * 10000 + i3 * 1000 + i4 * 100 + i5 * 10 + i6
    if (val < start) or (val > end):
        return 0, 0
    if (i1 != i2) and (i2 != i3) and (i3 != i4) and (i4 != i5) and (i5 != i6):
        return 0, 0
    if ((i1 == i2) and (i1 != i3)) or ((i2 == i3) and (i2 != i4) and (i2 != i1)) or ((i3 == i4) and (i3 != i5)and (i3 != i2)) or ((i4 == i5) and (i4 != i6)and (i4 != i3)) or ((i5 == i6)and (i5 != i4)):
        return 1, 1
    return 1, 0

for i1 in range(10):
    for i2 in range(i1, 10):
        for i3 in range(i2, 10):
            for i4 in range(i3, 10):
                for i5 in range(i4, 10):
                    for i6 in range(i5, 10):
                        v1, v2 = check_password(i1, i2, i3, i4, i5, i6)
                        part1 += v1
                        part2 += v2

print(f'{part1=}, {part2=}')
