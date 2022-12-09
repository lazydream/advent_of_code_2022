import math
from os.path import dirname, abspath


class Tree:

    def __init__(self, value: int, row: int, column: int):
        self.value = value
        self.row = row
        self.column = column
        self.visible = False

    def __repr__(self):
        return str(self.value)


class Grid:

    def __init__(self):
        self.trees = []

    def put_tree(self, tree: Tree):
        self.trees.append(tree)

    def get_column(self, col_num: int):
        column = []
        for tree in self.trees:
            if tree.column == col_num:
                column.append(tree)
        return sorted(column, key=lambda x: x.row)

    def get_row(self, row_num: int):
        row = []
        for tree in self.trees:
            if tree.row == row_num:
                row.append(tree)
        return sorted(row, key=lambda x: x.column)

    def __iter__(self):
        return (tree for tree in self.trees)

    def __repr__(self):
        return str(self.trees)

    def __len__(self):
        return int(math.sqrt(len(self.trees)))


with open(dirname(abspath(__file__)) + '/input.txt') as f:
    row = 0
    grid = Grid()
    for line in f:
        for col in range(len(line.strip())):
            grid.put_tree(Tree(int(line[col]), row, col))
            col += 1
        col = 0
        row += 1


length = len(grid)
for i in range(length):
    ith_row, ith_column = grid.get_row(i), grid.get_column(i)
    max_head_row, max_tail_row, max_head_column, max_tail_column = [-1] * 4
    for jth_tree in range(length):
        if ith_row[jth_tree].value > max_head_row:
            print(max_head_row)
            ith_row[jth_tree].visible = True
            max_head_row = ith_row[jth_tree].value
        if ith_row[-jth_tree - 1].value > max_tail_row:
            ith_row[-jth_tree - 1].visible = True
            max_tail_row = ith_row[-jth_tree - 1].value
        if ith_column[jth_tree].value > max_head_column:
            ith_column[jth_tree].visible = True
            max_head_column = ith_column[jth_tree].value
        if ith_column[-jth_tree - 1].value > max_tail_column:
            ith_column[-jth_tree - 1].visible = True
            max_tail_column = ith_column[-jth_tree - 1].value


amount = 0
for tree in grid:
    if tree.visible:
        amount += 1


print(amount)
