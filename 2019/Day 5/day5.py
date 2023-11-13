import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
str = f.read().split(',')

def run_intcode(str, input):
    s = [eval(i) for i in str]
    ip = 0
    op = 0
    while op != 99:
        op = s[ip] % 100
        p1 = int(s[ip] / 100) % 10
        p2 = int(s[ip] / 1000) % 10
        p3 = int(s[ip] / 10000) % 10
        match (op):
            case 1:
                v1 = s[ip + 1]
                v2 = s[ip + 2]
                if (p1 == 0):
                    v1 = s[s[ip + 1]]
                if (p2 == 0):
                    v2 = s[s[ip + 2]]
                s[s[ip + 3]] = v1 + v2
                ip += 4
            case 2:
                v1 = s[ip + 1]
                v2 = s[ip + 2]
                if (p1 == 0):
                    v1 = s[s[ip + 1]]
                if (p2 == 0):
                    v2 = s[s[ip + 2]]
                s[s[ip + 3]] = v1 * v2
                ip += 4
            case 3:
                print('Input')
                s[s[ip + 1]] = input
                ip += 2
            case 4:
                output = s[ip + 1]
                if (p1 == 0):
                        output = s[s[ip + 1]]
                ip += 2
            case 5:
                if (p1 == 0 and s[s[ip + 1]] != 0) or (p1 == 1 and s[ip + 1] != 0):
                    ip = s[ip + 2] if p2 == 1 else s[s[ip + 2]] 
                else:
                    ip += 3
            case 6:
                if (p1 == 0 and s[s[ip + 1]] == 0) or (p1 == 1 and s[ip + 1] == 0):
                    ip = s[ip + 2] if p2 == 1 else s[s[ip + 2]] 
                else:
                    ip += 3
            case 7:
                if (p1 == 0):
                    parm1 = s[s[ip + 1]]
                else:
                    parm1 = s[ip + 1]
                if (p2 == 0):
                    parm2 = s[s[ip + 2]]
                else:
                    parm2 = s[ip + 2]
                if parm1 < parm2:
                    s[s[ip + 3]] = 1
                else:
                    s[s[ip + 3]] = 0 
                ip += 4
            case 8:
                if (p1 == 0):
                    parm1 = s[s[ip + 1]]
                else:
                    parm1 = s[ip + 1]
                if (p2 == 0):
                    parm2 = s[s[ip + 2]]
                else:
                    parm2 = s[ip + 2]
                if parm1 == parm2:
                    s[s[ip + 3]] = 1
                else:
                    s[s[ip + 3]] = 0 
                ip += 4
            case 99:
                ip += 1
    return output

part1 = run_intcode(str, 1)
part2 = run_intcode(str, 5)

print(f'{part1=}, {part2=}')
