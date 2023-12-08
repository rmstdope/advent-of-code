import numpy as np
import copy
import itertools

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

class Rule:
    def __init__(self) -> None:
        self.rules = []
        self.num = -1
        pass

    def parse(self, s):
        self.rules = []
        rule = []
        self.num = int(s.split(': ')[0])
        for v in s.split(': ')[1].split(' '):
            if v == '|':
                self.rules.append(copy.deepcopy(rule))
                rule = []
            elif v[0] >= '0' and v[0] <= '9':
                rule.append(int(v))
            else:
                rule.append(v[1])
        self.rules.append(copy.deepcopy(rule))

rules = []
value_str = []
def parse_rules():
    global rules
    global value_str
    rules = []
    rule_str = []
    value_str = []
    parsing_rules = True
    for s in strs:
        if s == '':
            parsing_rules = False
        elif parsing_rules:
            rule_str.append(s)
        else:
            value_str.append(s)
    maxx = 0
    for s in rule_str:
        v = int(s.split(':')[0])
        maxx = max(maxx, v)
    for i in range(maxx + 1):    
        rules.append(Rule())
    for i in range(len(rule_str)):
        num = int(rule_str[i].split(':')[0])
        rules[num].parse(rule_str[i])

def recurse_rules():
    completed = []
    working = []
    for r in rules:
        if len(r.rules) > 0 and (r.rules[0][0] == 'a' or r.rules[0][0] == 'b'):
            completed.append(r)
        else:
            working.append(r)
    while len(completed) > 0:
        r = completed.pop()
        run = True
        while run:
            run = False
            for r2 in working:
                new_rules = []
                for rule in r2.rules:
                    if r.num in rule:
                        i = rule.index(r.num)
                        for insert_rule in r.rules:
                            new_rule = rule[0:i] + insert_rule + rule[i + 1:]
                            new_rules.append(new_rule)
                            run = True
                    else:
                        new_rules.append(rule)
                r2.rules = new_rules
        temp = working
        working = []
        for t in temp:
            move = True
            for r in t.rules:
                for v in r:
                    if isinstance(v, int):
                        move = False
            if move:
                completed.append(t)
            else:
                working.append(t)

def compress_rules():
    for r1 in rules:
        for i,r2 in enumerate(r1.rules):
            str = ''
            for c in r2:
                str += c
            r1.rules[i] = str

parse_rules()
recurse_rules()
compress_rules()

part1 = 0
for s in value_str:
    found = False
    if s in rules[0].rules:
        found = True
    if found:
        part1 +=1

parse_rules()
rules[8].parse('8: 42 | 42 8')
rules[11].parse('11: 42 31 | 42 11 31')
recurse_rules()

rules_8 = []
data = rules[8].rules[0:len(rules[8].rules) // 2]
for i,r in enumerate(data):
    s = ''
    for c in r:
        s += c
    rules_8.append(s)

rules_11 = []
data = rules[11].rules[len(rules[11].rules) // 2:]
for i,r in enumerate(data):
    s = ''
    for c in r:
        if isinstance(c, int):
            app = [s]
            s = ''
        else:
            s += c
    app.append(s)
    rules_11.append(app)

def remove_eights(num, s):
    for _ in range(num):
        found = False
        for r in rules_8:
            if s[0:len(r)] == r:
                s = s[len(r):]
                found = True
                break
        if not found:
            return -1
    return s

def remove_elevens(s):
    while True:
        found = False
        for r in rules_11:
            if s[0:len(r[0])] == r[0] and s[-len(r[1]):] == r[1]:
                s = s[len(r[1]):]
                s = s[0:-len(r[1])]
                found = True
        if not found or s == '':
            return s
    


part2 = 0
for s in value_str:
    # s = 'aaaabbaaaabbaaa'
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
    num_8 = 1
    while True:
        s_test = s
        s_test = remove_eights(num_8, s_test)
        if not isinstance(s_test, str) or s_test == '':
            break
        s_test = remove_elevens(s_test)
        if s_test == '':
            part2 += 1
            # print(s)
            break
        num_8 += 1

# for s in value_str:
#     num_8 = 0
#     shortened = True
#     while shortened and len(s) > 0:
#         shortened = False
#         for r in rules_11:
#             if s[0:len(r[0])] == r[0] and s[-len(r[1]):] == r[1]:
#                 s = s[len(r[1]):]
#                 s = s[0:-len(r[1])]
#                 shortened = True
#     if len(s) == 0:
#         part2 += 1

#     found = False
#     for r in rules:
#         if s in r.rules:
#             found = True
#     if found:
#         part2 +=1
#     s = 'babbbbaabbbbbabbbbbbaabaaabaaa'
#     # s = 'bbbbbbbaaaabbbbaaabbabaaa'
#     # s = 'bbbababbbbaaaaaaaabbababaaababaabab'

print(f'{part1=}, {part2=}')

