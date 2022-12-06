# https://adventofcode.com/2022/day/6
import os
from collections import deque

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")


with open(input_file, "r") as file:
    line = file.readline().strip()
    sop_marker = deque([])

    for i, c in enumerate(line):
        if c not in sop_marker:
            if len(sop_marker) == 13:
                print(i + 1)
                break
            else:
                sop_marker.append(c)
        else:
            left_char = sop_marker.popleft()
            while left_char != c:
                left_char = sop_marker.popleft()
            sop_marker.append(c)
