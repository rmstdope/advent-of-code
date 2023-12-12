import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')

ok_configs = {}

def get_num_matches(data, broken, is_continued):
    
    key = (data, broken, is_continued)
    
    if key not in ok_configs:
        if sum(broken) == 0:
            if '#' not in data:
                ok_configs[key] = 1
            else:
                ok_configs[key] = 0
        elif data == '':
                ok_configs[key] = 0
        elif data[0] == '#':
            if not is_continued or broken[0] != 0:
                ok_configs[key] = get_num_matches(data[1:], (broken[0] - 1, *broken[1:]), True)
            else:
                ok_configs[key] = 0
        elif data[0] == ".":
            if broken[0] == 0:
                ok_configs[key] = get_num_matches(data[1:], broken[1:], False)
            elif not is_continued:
                ok_configs[key] = get_num_matches(data[1:], broken, False)
            else:
                ok_configs[key] = 0
        elif is_continued:
            if broken[0] == 0:
                ok_configs[key] = get_num_matches(data[1:], broken[1:], False)
            else:
                ok_configs[key] = get_num_matches(data[1:], (broken[0] - 1, *broken[1:]), True)
        else:
            ok_configs[key] = get_num_matches(data[1:], broken, False) + get_num_matches(data[1:], (broken[0] - 1, *broken[1:]), True)

    return ok_configs[key]

strs = f.read().splitlines()
part1 = 0
part2 = 0
for s in strs:
    data, broken = s.split(' ')
    broken = tuple(map(int, broken.split(",")))

    part1 += get_num_matches(data, broken, False)

    data = data + '?' + data + '?' + data + '?' + data + '?' + data
    broken = broken + broken + broken + broken + broken
    part2 += get_num_matches(data, broken, False)

print(f'{part1=}, {part2=}')
