"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example:
    [[0, 1, 0, 0, 1],
     [0, 1, 0, 1, 0],
     [1, 0, 1, 1, 0],
     [1, 1, 1, 1, 0]
     [1, 0, 1, 1, 0]]

min_length = 9

Questions:
    - Cells can only be 1 or 0? Yes


Approach:
    - Check that top left and bottom right cells are clear. If not, return -1
    - Iterate over the grid and set all 1s to None
    - Do a BFS from the top right with the following:
        - Maintain the minimum distance to the current cell.
        - If the adjacent cell has less distance than would be given from current route, add it to the queue
        - When queue is processed, we should have the minimum distance at the bottom right of the grid


"""
import collections

from math import inf


def shortest_distance(grid):
    if grid[0][0] or grid[-1][-1]:
        return -1

    # O(N^2) time and O(1) space.
    n = len(grid)
    for row in range(n):
        for col in range(n):
            if grid[row][col]:
                grid[row][col] = None
            else:
                grid[row][col] = inf


    queue = collections.deque()
    queue.append((1, 0, 0))
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (-1, -1), (1, -1), (-1, 1))

    # O(N^2) time and O(N^2) space for queue.
    while queue:
        num_visited, curr_row, curr_col = queue.popleft()

        if num_visited >= grid[curr_row][curr_col]:
            continue

        grid[curr_row][curr_col] = num_visited

        for row_inc, col_inc in directions:
            next_row, next_col = curr_row + row_inc, curr_col + col_inc

            if (not 0 <= next_row < n
                or not 0 <= next_col < n
                or grid[next_row][next_col] is None
                or grid[next_row][next_col] <= num_visited + 1):
                continue

            queue.appendleft((num_visited + 1, next_row, next_col))

    return grid[-1][-1] if not grid[-1][-1] == inf else -1
        
