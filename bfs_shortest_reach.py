#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque
#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

class Graph:

    def __init__(self, num_vertices):
        self.table = [[] for _ in range(num_vertices)]

    def add_edge(self, from_vert, to_vert):
        self.table[from_vert - 1].append(to_vert - 1)
        self.table[to_vert - 1].append(from_vert - 1)

    def __getitem__(self, key):
        return self.table[key]


def bfs(n, m, edges, s):
    # Write your code here

    graph = Graph(n)

    for from_vertex, to_vertex in edges:
        graph.add_edge(from_vertex, to_vertex)

    print(graph.table)

    result = [-1] * (n - 1)
    queue = deque()
    queue.append((0, s - 1))

    visited = set()

    while queue:
        distance, curr_vert = queue.popleft()

        if curr_vert in visited:
            continue

        visited.add(curr_vert)

        #print(result, distance, curr_vert)
        if curr_vert > s - 1:
            result[curr_vert - 1] = 6 * distance
        elif curr_vert < s - 1:
            result[curr_vert] = 6 * distance

        for adj_vert in graph[curr_vert]:
            if not adj_vert in visited:
                queue.append((distance + 1), adj_vert))

    #print(result)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
