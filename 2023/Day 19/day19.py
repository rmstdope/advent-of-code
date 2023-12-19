import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().strip()

s = strs.split('\n\n')

class SubRule:
    def __init__(self, s) -> None:
        if ':' in s:
            self.letter = s[0]
            self.comp = s[1]
            x = s[2:].split(':')
            self.value = int(x[0])
            self.destination = x[1]
        else:
            self.destination = s
            self.comp = ''
    
    def matches(self, x, m, a, s):
        if self.comp == '':
            return True
        else:
            match self.letter:
                case 'x':
                    compv = x
                case 'm':
                    compv = m
                case 'a':
                    compv = a
                case 's':
                    compv = s
            if (self.comp == '>' and compv > self.value) or (self.comp == '<' and compv < self.value):
                return True
        return False

    def subint(self, x, m, a, s):
        match self.letter:
            case 'x':
                if self.comp == '>':
                    return (max(x[0], self.value + 1), x[1]), m, a, s
                else:
                    return (x[0], min(self.value - 1, x[1])), m, a, s
            case 'm':
                if self.comp == '>':
                    return x, (max(m[0], self.value + 1), m[1]), a, s
                else:
                    return x, (m[0], min(self.value - 1, m[1])), a, s
            case 'a':
                if self.comp == '>':
                    return x, m, (max(a[0], self.value + 1), a[1]), s
                else:
                    return x, m, (a[0], min(self.value - 1, a[1])), s
            case 's':
                if self.comp == '>':
                    return x, m, a, (max(s[0], self.value + 1), s[1])
                else:
                    return x, m, a, (s[0], min(self.value - 1, s[1]))

    def subintinv(self, x, m, a, s):
        match self.letter:
            case 'x':
                if self.comp == '>':
                    return (x[0], min(self.value, x[1])), m, a, s
                else:
                    return (max(x[0], self.value), x[1]), m, a, s
            case 'm':
                if self.comp == '>':
                    return x, (m[0], min(self.value, m[1])), a, s
                else:
                    return x, (max(m[0], self.value), m[1]), a, s
            case 'a':
                if self.comp == '>':
                    return x, m, (a[0], min(self.value, a[1])), s
                else:
                    return x, m, (max(a[0], self.value), a[1]), s
            case 's':
                if self.comp == '>':
                    return x, m, a, (s[0], min(self.value, s[1]))
                else:
                    return x, m, a, (max(s[0], self.value), s[1])

class Rule:
    def __init__(self, s) -> None:
        x = s.split('{')
        self.name = x[0]
        rules = x[1][:len(x[1]) - 1]
        r = rules.split(',')
        self.subrules = []
        for rule in r:
            self.subrules.append(SubRule(rule))

    def process(self, x, m, a, s):
        for r in self.subrules:
            if r.matches(x, m, a, s):
                # print('Matches ', r.destination)
                return r.destination
        assert('Error')


rules = {}
for r in s[0].splitlines():
    rule = Rule(r)
    rules[rule.name] = rule

part1 = 0
for part in s[1].splitlines():
    part = part[1:len(part) - 1]
    part = part.split(',')
    x = int(part[0][2:])
    m = int(part[1][2:])
    a = int(part[2][2:])
    s = int(part[3][2:])
    workflow = rules['in']
    while True:
        result = workflow.process(x, m, a, s)
        if (result == 'A'):
            part1 += x + m + a + s
            break
        elif (result == 'R'):
            break
        workflow = rules[result]

x_ok = []
m_ok = []
a_ok = []
s_ok = []
part2 = 0
process = [((1, 4000), (1, 4000), (1, 4000), (1, 4000), 'in')]
while process:
    p = process.pop()
    x = p[0]
    m = p[1]
    a = p[2]
    s = p[3]
    workflow = rules[p[4]]
    for r in workflow.subrules:
        if r.comp == '':
            if r.destination == 'A':
                x_ok.append(x)
                m_ok.append(m)
                a_ok.append(a)
                s_ok.append(s)
            elif r.destination == 'R':
                break
            else:
                process.append((x, m, a, s, r.destination))
        else:
            newx, newm, newa, news = r.subint(x, m, a, s)
            x, m, a, s = r.subintinv(x, m, a, s)
            if r.destination == 'A':
                x_ok.append(newx)
                m_ok.append(newm)
                a_ok.append(newa)
                s_ok.append(news)
            elif r.destination == 'R':
                pass
            else:
                process.append((newx, newm, newa, news, r.destination))

for i in range(len(x_ok)):
    x = 0
    m = 0
    a = 0
    s = 0
    if x_ok[i][1] >= x_ok[i][0]:
        x = x_ok[i][1] - x_ok[i][0] + 1
    if m_ok[i][1] >= m_ok[i][0]:
        m = m_ok[i][1] - m_ok[i][0] + 1
    if a_ok[i][1] >= a_ok[i][0]:
        a = a_ok[i][1] - a_ok[i][0] + 1
    if s_ok[i][1] >= s_ok[i][0]:
        s = s_ok[i][1] - s_ok[i][0] + 1
    part2 += x * m * a * s

print(f'{part1=}, {part2=}')
