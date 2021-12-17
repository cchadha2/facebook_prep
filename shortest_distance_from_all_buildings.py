from collections import deque
from math import inf

# From each 0.
def minimum_distance(grid):

    m, n = len(grid), len(grid[0])
    stack = []

    num_buildings = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1:
                num_buildings += 1
            elif not grid[row][col]:
                stack.append((0, row, col))

    minimum_distance = inf
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    # O(N^2 * M^2) as we may have only 1 house in our grid, no obstacles,
    # and do a BFS from all zeros.
    while stack:

        queue = deque()
        # O(NM) for BFS as at most NM cells are visited.
        visited = set()
        buildings_visited = curr_distance = 0

        queue.append(stack.pop())

        while queue and len(buildings_visited) < num_buildings:
            distance, row, col = queue.popleft()

            if (row, col) in visited:
                continue

            visited.add((row, col))

            if grid[row][col] == 1:
                curr_distance += distance
                buildings_visited += 1
                continue

            for row_inc, col_inc in directions:
                next_row, next_col = row + row_inc, col + col_inc
                if (not 0 <= next_row < m or not 0 <= next_col < n):
                    continue

                if grid[next_row][next_col] <= 1:
                    queue.append((distance + 1, next_row, next_col))


        if buildings_visited == num_buildings:
            minimum_distance = min(minimum_distance, curr_distance)


    return -1 if minimum_distance == inf else minimum_distance

# From each house.
def minimum_distance(grid):

    m, n = len(grid), len(grid[0])
    stack = []
    num_buildings = 0

    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1:
                grid[row][col] = "H"
                stack.append((0, row, col))
                num_buildings += 1
            elif grid[row][col] == 2:
                grid[row][col] = None
            else:
                grid[row][col] = [0, 0]


    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    minimum_distance = inf
    while stack:
        visited = set()
        queue = deque((stack.pop(), ))

        while queue:
            distance, row, col = queue.popleft()

            if (row, col) in visited:
                continue

            visited.add((row, col))

            if grid[row][col] is None:
                continue

            if type(grid[row][col]) is list:
                grid[row][col][0] += distance
                grid[row][col][1] += 1

                if (grid[row][col][1] == num_buildings
                    and grid[row][col][0] < minimum_distance):
                    minimum_distance = grid[row][col][0]


            for row_inc, col_inc in directions:
                next_row, next_col = row + row_inc, col + col_inc

                if (not 0 <= next_row < m
                    or not 0 <= next_col < n
                    or grid[next_row][next_col] == "H"):
                    continue

                queue.append((distance + 1, next_row, next_col))

    return minimum_distance if minimum_distance != inf else -1


# Optimized from each house (this passes Leetcode tests).
def minimum_distance(grid):
    m, n = len(grid), len(grid[0])
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    total = [[0] * n for _ in range(m)]
    empty_land = 0
    minimum_distance = inf

    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1:
                minimum_distance = inf

                queue = deque(((row, col), ))

                distance = 0
                while queue:
                    distance += 1

                    levels = len(queue)
                    for _ in range(levels):
                        curr_row, curr_col = queue.popleft()

                        for row_inc, col_inc in directions:
                            next_row, next_col = curr_row + row_inc, curr_col + col_inc

                            if (not 0 <= next_row < m
                                or not 0 <= next_col < n
                                or grid[next_row][next_col] != empty_land):
                                continue

                            grid[next_row][next_col] -= 1
                            total[next_row][next_col] += distance

                            queue.append((next_row, next_col))
                            minimum_distance = min(minimum_distance, total[next_row][next_col])

                empty_land -= 1

    return minimum_distance if minimum_distance != inf else -1
