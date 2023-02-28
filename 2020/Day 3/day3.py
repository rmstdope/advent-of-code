f = open('input.txt')
str = f.read().splitlines()


def slope(dx, dy):
    res = 0
    x, y = 0, 0
    while y < len(str):
        if (str[y][x % len(str[y])]) == '#':
            res += 1
        x += dx
        y += dy
    return res


part1 = slope(3, 1)
part2 = slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2)

print(f'{part1=}, {part2=}')
