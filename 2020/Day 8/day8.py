f = open('input.txt')
str = f.read().splitlines()

inst = []
for s in str:
    inst.append((s[:3], int(s[3:])))


def execute():
    i = 0
    acc = 0
    executed = set()
    while (i not in executed) and (i < len(inst)):
        executed.add(i)
        cmd, num = inst[i]
        if cmd == 'acc':
            acc += num
            i += 1
        elif cmd == 'jmp':
            i += num
        elif cmd == 'nop':
            i += 1
    return (i, acc)


(i, part1) = execute()
for i in range(len(inst)):
    old = inst[i]
    if old[0] == 'jmp':
        inst[i] = ('nop', old[1])
    if old[0] == 'nop':
        inst[i] = ('jmp', old[1])
    (ins, part2) = execute()
    if ins == len(inst):
        break
    inst[i] = old

print(f'{part1=}, {part2=}')
