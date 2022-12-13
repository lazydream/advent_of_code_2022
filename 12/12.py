# https://adventofcode.com/2022/day/12
import os
from string import ascii_lowercase

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")
height_map = {c: i for i in ascii_lowercase}
height_map["S"] = height_map["a"]
height_map["E"] = height_map["z"]

grid = []
visited = set()
start_position = None
end_position = None
with open(input_file, "r") as file:
    for i, line in enumerate(file):
        line = line.strip()
        row = []
        for j, c in enumerate(line):
            row.append(c)
            if c == "S":
                start_position = (i, j)
            if c == "E":
                end_position = (i, j)
        grid.append(row)

distance_map = {
    start_position: 0
}

def _find_possible_moves(i: int, j: int) -> list[tuple[int, int]]:
    cur_height = height_map[grid[i][j]]
    possible_moves = []
    for ni, nj in ((i+1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if ni >= 0 and nj >= 0:
            if cur_height >= height_map[grid[ni][nj]] - 1:
                possible_moves.append((ni, nj))

def djkstra_req(i: int, j: int) -> None:
    cur = grid[i, j]
    available_neighbours = _find_possible_moves(i, j)
    for (ni, nj) in available_neighbours:
        if (ni, nj) not in visited:
            cur_distance = distance_map[i, j] + 1
            distance_map[ni, nj] = cur_distance
            visited.add(ni, nj)
