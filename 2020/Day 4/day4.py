f = open('input.txt')
str = f.read().splitlines()

# prepare one liners
s = ''
l = []
for sub in str:
    if sub == '':
        l.append(s)
        s = ''
    else:
        s += sub if s == '' else (' ' + sub)
l.append(s)


def check_field(f, d):
    if f == 'byr':
        if int(d) < 1920 or int(d) > 2002:
            return 0
    elif f == 'iyr':
        if int(d) < 2010 or int(d) > 2020:
            return 0
    elif f == 'eyr':
        if int(d) < 2020 or int(d) > 2030:
            return 0
    elif f == 'hgt':
        unit = d[len(d) - 2:]
        data = d[:len(d) - 2]
        # print(f'{unit=}, {data=}')
        if unit == 'cm':
            if int(data) < 150 or int(data) > 193:
                return 0
        elif unit == 'in':
            if int(data) < 59 or int(data) > 76:
                return 0
        else:
            return 0
    elif f == 'hcl':
        if len(d) != 7 or d[0] != '#':
            return 0
        for c in d[1:]:
            if (c < 'a' or c > 'f') and (c < '0' or c > '9'):
                return 0
    elif f == 'ecl':
        if d != 'amb' and d != 'blu' and d != 'brn' and d != 'gry' and d != 'grn' and d != 'hzl' and d != 'oth':
            return 0
    elif f == 'pid':
        if len(d) != 9:
            return 0
        for c in d[1:]:
            if (c < '0' or c > '9'):
                return 0
    elif f == 'cid':
        return 1
    else:
        return 0
    return 1


part1, part2 = 0, 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
for s in l:
    bits1 = 0
    allok = True
    for f in s.split(' '):
        bits1 += 1 << fields.index(f.split(':')[0])
        allok = allok and check_field(f.split(':')[0], f.split(':')[1])

    bits1 &= 127
    if bits1 == 127:
        part1 += 1
        if allok:
            part2 += 1

print(f'{part1=}, {part2=}')
