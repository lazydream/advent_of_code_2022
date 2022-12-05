# https://adventofcode.com/2022/day/5
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")

stacks = [
    [
        "D", "L", "J", "R", "V", "G", "F"
    ],
    [
        "T", "P", "M", "B", "V", "H", "J", "S"
    ],
    [
        "V", "H", "M", "F", "D", "G", "P", "C"
    ],
    [
        "M", "D", "P", "N", "G", "Q"
    ],
    [
        'J', "L", "H", "N", "F"
    ],
    [
        "N", "F", "V", "Q", "D", "G", "T", "Z"
    ],
    [
        "F", "D", "B", "L"
    ],
    [
        "M", "J", "B", "S", "V", "D", "N"
    ],
    [
        "G", "L", "D"
    ]
]


with open(input_file, "r") as file:
    for i, line in enumerate(file):
        if i < 10:
            continue

        line = line.replace("\n", "")
        args = line.split(" ")
        amount, stack_from, stack_to = int(args[1]), int(args[3]), int(args[5])

        while amount > 0:
            stacks[stack_to - 1].append(stacks[stack_from - 1].pop())
            amount -= 1
        

answer = [stack.pop() for stack in stacks]

print("".join(answer))