# https://adventofcode.com/2022/day/9
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")

visited_1 = {(0, 0)}
visited_2 = {(0, 0)}


def align_tail(head, tail, track=0):
    c_map = {
        1: 0,
        0: 1
    }
    for i in range(2):
        current_diff = abs(head[i] - tail[i])
        j = c_map[i]
        opposite_diff = abs(head[j] - tail[j])
        if current_diff == 2:
            tail[i] = tail[i] - 1 if tail[i] > head[i] else tail[i] + 1
            if opposite_diff in (1,2):
                tail[j] = tail[j] - 1 if tail[j] > head[j] else tail[j] + 1
            if track == 1:
                visited_1.add((tail[0], tail[1]))
            if track == 2:
                visited_2.add((tail[0], tail[1]))

with open(input_file, "r") as file:
    knots = [[0, 0] for _ in range(10)]

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
            align_tail(head, tail, track=1)
            for i in range(len(knots) - 2, 1, -1):
                local_head = knots[i]
                local_tail = knots[i - 1]
                align_tail(local_head, local_tail)

            latter_head = knots[1]
            latter_tail = knots[0]
            align_tail(latter_head, latter_tail, track=2)

print(len(visited_1))
print(len(visited_2))
