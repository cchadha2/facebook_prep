#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

class Graph:

    def __init__(self, snakes, ladders):
        self.board = [[] for _ in range(100)]
        snakes = dict(snakes)
        ladders = dict(ladders)

        for idx in range(99):
            for adj_idx in range(idx + 1, min(100, idx + 7)):
                if adj_idx in snakes:
                    self.board[idx].append(snakes[adj_idx])
                elif adj_idx in ladders:
                    self.board[idx].append(ladders[adj_idx])
                else:
                    self.board[idx].append(adj_idx)

    def __getitem__(self, key):
        return self.board[key]


def quickestWayUp(ladders, snakes):

    graph = Graph(snakes, ladders)

    queue = deque()
    queue.append((0, 0))

    visited = set()

    while queue:
        distance, vert = queue.popleft()

        if vert in visited:
            continue
        elif vert == 99:
            return distance

        visited.add(vert)

        for adj_vert in graph[vert]:
            if not adj_vert in visited:
                queue.append((distance + 1, adj_vert))

    return -1


if __name__ == '__main__':
    ladders = [[32, 63], [42, 68], [12, 98]]
    snakes = [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]

    print(quickestWayUp(ladders, snakes))
