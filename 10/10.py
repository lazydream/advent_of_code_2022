# https://adventofcode.com/2022/day/10
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")

x = 1
s = 0
rows = []
row = []


def check_strength(cycle):
    global s
    if (cycle - 20) % 40 == 0 and cycle <= 220:
        print(cycle, x, cycle * x)
        s += x*cycle


def print_row(cycle):
    global row
    global rows
    row_cycle = (cycle - 1) % 40
    if row_cycle in {x-1, x, x + 1}:
        d = "#"
    else:
        d = "."
    if row_cycle < 39:
        row.append(d)
    else:
        rows.append("".join(row))
        row = []


with open(input_file, "r") as file:
    cycle = 1
    row = []
    for i, line in enumerate(file):
        line = line.strip().split(" ")

        if line[0] == "noop":
            cycle += 1
            check_strength(cycle)
            print_row(cycle)
        else:
            add_x = int(line[1])
            cycle += 1
            check_strength(cycle)
            print_row(cycle)
            cycle += 1
            x += add_x
            check_strength(cycle)
            print_row(cycle)

print(s)
img = "".join([f'{row}\n' for row in rows])
print(img) 
