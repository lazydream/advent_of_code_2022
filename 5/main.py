from collections import deque
from os.path import dirname, abspath
import re


d = {}
IntVar = 1 | 2


def deque_(position: int) -> deque:
    if position not in d.keys():
        d[position] = deque()
    return d[position]


def move(amount, from_, to_):
    for _ in range(amount):
        d[to_].append(d[from_].pop())


def move_2(amount, from_, to_):
    cranes = []
    for _ in range(amount):
        cranes.append(d[from_].pop())
    for crane in reversed(cranes):
        d[to_].append(crane)


def task(num_task: IntVar = 1):
    func = move if num_task == 1 else move_2
    with open(dirname(abspath(__file__)) + '/input.txt') as f:
        for line in f:
            if line.startswith('move'):
                pattern = r' ([0-9]+)'
                numbers = re.findall(pattern, line)
                func(*map(int, numbers))

            elif not line.strip():
                for k, v in d.items():
                    d[k] = deque(reversed(v))
            else:
                substring = ''
                for i in range(len(line)):
                    if (i + 1) % 4 == 0:
                        stack = (i + 1) // 4
                        if substring[1].isalpha():
                            deque_(stack).append(substring[1])
                        substring = ''
                    else:
                        substring += line[i]


task(2)

answer = ''
for i in range(1, len(d) + 1):
    answer += d[i].pop()

print(answer)
