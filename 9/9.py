# https://adventofcode.com/2022/day/9
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")

tail_visited_positions = 0

with open(input_file, "r") as file:
  i, j, ti, tj = "i", "j", "ti", "tj"

  visited = set((0, 0))

  tail_map = {
    i: ti,
    j: tj
  }

  pp = {
    i: j,
    ti: tj
  }

  p = {
    i: 0,
    j: 0,
    ti: 0,
    tj: 0,
  }
  
  for line in file:
    line = line.strip().split(" ")
    direction, steps = line[0], int(line[1])
    if direction == "L":
      vector = (i, -1)
    elif direction == "R":
      vector = (i, 1)
    elif direction == "U":
      vector = (j, 1)
    elif direction == "D":
      vector = (j, -1)

    for k in range(steps):
      p[vector[0]] += 1 * vector[1]
      i_diff = abs(p[i] - p[ti])
      j_diff = abs(p[j] - p[tj])
      if not(i_diff == 2 or j_diff == 2):
        continue
      if i_diff == 2 and j_diff == 1:
        p[ti] += 1 * vector[1]
        p[tj] = p[j]
        visited.add((p[ti], p[tj]))
        continue
      if j_diff == 2 and i_diff == 1:
        p[tj] += 1 * vector[1]
        p[ti] = p[i]
        visited.add((p[ti], p[tj]))
        continue

      p[tail_map[vector[0]]] += 1 * vector[1]
      visited.add((p[ti], p[tj]))
      
print(len(visited))