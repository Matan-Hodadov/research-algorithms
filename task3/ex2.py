from sys import maxsize
from itertools import permutations

from typing import Callable, Any


# from bins import *
# import outputtypes as out


def partition(algorithm: Callable, items: list, starting_vertex: int, outputtype: str):
    if isinstance(items[0], tuple):  # items is a dict mapping an item to its value.
        items = sorted(items, key=lambda x: x[0])
        temp_l = []
        graph = []
        [temp_l.append(0) for i in range(items[-1][1] + 1)]
        [graph.append(temp_l.copy()) for i in range(items[-1][1] + 1)]
        for tup in items:
            graph[tup[0]][tup[1]] = tup[2]
            graph[tup[1]][tup[0]] = tup[2]
    else:  # items is a list
        graph = items

    return algorithm(graph, starting_vertex, outputtype)


def allCombinationsAlgorithm(graph: list, s: int, outputtype: str):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        if current_pathweight < min_path:
            path = [s]
            [path.append(j) for j in i]
            path.append(s)
            min_path = current_pathweight

        # # update minimum
        # min_path = min(min_path, current_pathweight)
    if outputtype == "path":
        return path
    elif outputtype == "distance":
        return min_path
    raise ValueError


def sillyAlgorithm(graph: list, s, outputtype):
    visited = [s]
    dist = 0
    while len(visited) < len(graph):
        temp = graph[visited[-1]].copy()
        temp.sort()
        for i in range(1, len(graph)):
            shortest_dist = temp[i]
            vertex_inx = graph[visited[-1]].index(shortest_dist)
            if vertex_inx not in visited:
                visited.append(vertex_inx)
                dist += shortest_dist
                break
    temp = graph[visited[-1]].copy()
    dist += temp[s]
    visited.append(s)

    if outputtype == "path":
        return visited
    elif outputtype == "distance":
        return dist
    raise ValueError


if __name__ == "__main__":
    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    # distance should return 80
    # path should return [0, 1, 3, 2, 0]
    print(partition(allCombinationsAlgorithm, graph, s, "distance"))
    print(partition(allCombinationsAlgorithm, graph, s, "path"))
    print(partition(sillyAlgorithm, graph, s, "distance"))
    print(partition(sillyAlgorithm, graph, s, "path"))

    # different type of input
    graph = [(0, 1, 3.1623), (0, 2, 4.1231), (0, 3, 5.8310), (0, 4, 4.2426), (0, 5, 5.3852), (0, 6, 4.0000), (0, 7, 2.2361),
             (1, 2, 1.0000), (1, 3, 2.8284), (1, 4, 2.0000), (1, 5, 4.1231), (1, 6, 4.2426), (1, 7, 2.2361),
             (2, 3, 2.2361), (2, 4, 2.2361), (2, 5, 4.4721), (2, 6, 5.0000), (2, 7, 3.1623),
             (3, 4, 2.0000), (3, 5, 3.6056), (3, 6, 5.0990), (3, 7, 4.1231),
             (4, 5, 2.2361), (4, 6, 3.1623), (4, 7, 2.2361),
             (5, 6, 2.2361), (5, 7, 3.1623),
             (6, 7, 2.2361)]

    # should return 17.3428
    print(partition(allCombinationsAlgorithm, graph, s, "distance"))
    # should return [0, 1, 2, 3, 4, 5, 6, 7, 0]
    print(partition(allCombinationsAlgorithm, graph, s, "path"))
    # should return 23.2334
    print(partition(sillyAlgorithm, graph, s, "distance"))
    # should return [0, 7, 2, 1, 4, 6, 5, 3, 0]
    print(partition(sillyAlgorithm, graph, s, "path"))

