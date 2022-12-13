# https://adventofcode.com/2022/day/12
import os
from string import ascii_lowercase

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")
height_map = {c: i for i, c in enumerate(ascii_lowercase)}
height_map["S"] = height_map["a"]
height_map["E"] = height_map["z"]


start = None
starts = []
end = None
grid = []
with open(input_file, "r") as file:
    for i, line in enumerate(file):
        row = []
        for j, c in enumerate(line.strip()):
            if c == "S":
                start = (i, j)
                starts.append(start)
            elif c == "E":
                end = (i, j)
            elif c == "a":
                starts.append((i, j))
            row.append(c)
        grid.append(row)


def flood(dist_map, layer, current_distance) -> None:
    connections = set()
    for i, j in layer:
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
            if ni >= 0 and ni < len(grid) and nj > 0 and nj < len(grid[0]) and height_map[grid[i][j]] >= height_map[grid[ni][nj]] - 1 and (ni, nj) not in dist_map:
                connections.add((ni, nj))

    for i, j in connections:
        dist_map[(i, j)] = current_distance + 1
    if connections:
        flood(dist_map, connections, current_distance + 1)


def distance(start, end):
    dist_map = {
        start: 0
    }
    flood(dist_map, {start}, 0)
    return dist_map.get(end, None)


print(distance(start, end))
print(min(distance(start, end) for start in starts if distance(start, end)))
