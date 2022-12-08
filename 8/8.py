# https://adventofcode.com/2022/day/8
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")

grid = []
with open(input_file, "r") as file:
    for line in file:
        row = [int(c) for c in line.strip()]
        grid.append(row)    

rows = len(grid)
cols = len(grid[0])

visible_trees = (cols * 2 + rows * 2) - 4

def _get_slices(i, j):
    slice_right = grid[i][j + 1:]
    slice_bottom = [row[j] for row in grid[i+1:]]

    slice_left_ordered = []
    for k in range(j - 1, -1, -1):
        slice_left_ordered.append(grid[i][k])
    
    slice_top_ordered = []
    vertical_sliced_grid = grid[:i]
    for k in range(i - 1, -1, -1):
        slice_top_ordered.append(vertical_sliced_grid[k][j])

    return slice_left_ordered, slice_right, slice_bottom, slice_top_ordered

def is_tree_visible(i, j):
    tree_height = grid[i][j]
    slice_left, slice_right, slice_bottom, slice_top = _get_slices(i, j)
    if (max(slice_left) < tree_height or 
        max(slice_right) < tree_height or 
        max(slice_top) < tree_height or 
        max(slice_bottom) < tree_height):
        return True

def scenic_score(i, j):
    tree_height = grid[i][j]
    scenic_score = 1
    for slice in _get_slices(i, j):
        current_score = 0
        for t in slice:
            current_score += 1
            if t >= tree_height:
                break
        scenic_score *= current_score
    return scenic_score

max_scenic_score = 0
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if is_tree_visible(i, j):
            visible_trees += 1
        max_scenic_score = max(scenic_score(i, j), max_scenic_score)

print("Part 1", visible_trees)
print("Part 2", max_scenic_score)
