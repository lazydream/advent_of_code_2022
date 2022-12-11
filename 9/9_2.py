# https://adventofcode.com/2022/day/9
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input_1.txt")

visited = {(0, 0)}


def align_tail(head, tail, track=False):
    i_diff = abs(head[0] - tail[0])
    j_diff = abs(head[1] - tail[1])
    if i_diff == 2:
        tail[0] = head[0] - 1
        if j_diff == 1:
            tail[1] = head[1]
        if track:
            visited.add((tail[0], tail[1]))
    elif j_diff == 2:
        tail[1] = head[1] - 1
        if i_diff == 1:
            tail[0] = head[0]
        if track:
            visited.add((tail[0], tail[1]))


with open(input_file, "r") as file:
    knots = [[0, 0] for _ in range(9)]

    for line in file:
        line = line.strip().split(" ")
        direction, steps = line[0], int(line[1])
        if direction == "L":
            vector = (0, -1)
        elif direction == "R":
            vector = (0, 1)
        elif direction == "U":
            vector = (1, 1)
        elif direction == "D":
            vector = (1, -1)

        for k in range(steps):
            head = knots[len(knots) - 1]
            tail = knots[len(knots) - 2]
            head[vector[0]] += 1 * vector[1]
            align_tail(head, tail)
            print("step")
            for i in range(len(knots) - 2, 1, -1):
                local_head = knots[i]
                local_tail = knots[i - 1]
                align_tail(local_head, local_tail)

            latter_head = knots[1]
            latter_tail = knots[0]
            align_tail(latter_head, latter_tail, track=True)

print(len(visited))
print(knots)
