# https://adventofcode.com/2022/day/12
import os
from string import ascii_lowercase

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")
height_map = {c: i for i in ascii_lowercase}
height_map["S"] = height_map["a"]
height_map["E"] = height_map["z"]
graph_map = dict()


class Graph:
    def __init__(self, val: str, key: tuple[int, int]) -> None:
        self.val = val
        self.key = key
        self.adjacent = dict()
    
    def add_neighbour(self, graph: 'Graph') -> None:
        self.adjacent[graph.key] = graph

    def has_neighbour(self, key: tuple[int, int]) -> bool:
        return key in self.adjacent


def _get_connected_graphs(i: int, j: int) -> list[Graph]:
    cur_height = height_map[grid[i][j]]
    connected_graphs = []
    for ni, nj in ((i+1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if ni >= 0 and nj >= 0:
            if cur_height >= height_map[grid[ni][nj]] - 1:
                graph = _get_or_create_graph(ni, nj)
                connected_graphs.append(graph)


def _get_or_create_graph(i, j) -> Graph:
    if (i, j) not in graph_map:
        graph = Graph(c, (i, j))
        graph_map[(i, j)] = graph
    else:
        graph = graph_map[(i, j)]
    return graph


grid = []
visited = set()
start_graph = None
# end_position = None
with open(input_file, "r") as file:
    for i, line in enumerate(file):
        line = line.strip()
        for j, c in enumerate(line):
            graph = _get_or_create_graph(i, j)
            for connected_graph in _get_connected_graphs(i, j):
                if not graph.has_neighbour(connected_graph.key):
                    graph.add_neighbour(graph)
                else:
                    print("check is needed")
            if graph.val == "S":
                start_graph = graph


distance_map = {
    start_graph.key: 0
}


def djkstra_req(graph: Graph) -> None:
    for connected_graph in graph.adjacent.values():
        if connected_graph.key not in visited:
            cur_distance = distance_map[graph.key] + 1
            distance_map[connected_graph.key] = cur_distance
    visited.add(graph.key)
