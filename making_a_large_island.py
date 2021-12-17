"""

1 1 1 0 1
1 0 1 0 0
1 1 0 1 1
1 1 0 1 1
0 1 0 0 0

Maximum is joining island with sum 10 and island with sum 4 to create an island with sum 15 (added 1).

Approach:
    - Do a DFS on each 1 to find the sum of each island. Add its (row, col) to a stack
      which we will subsequently iterate over to do the next step.
    - Set all of that island's values to a tuple of (island_id, sum)
    - Iterate over each 0 and find the max value you would obtain by changing it to a 0.
      This involves checking 4 directionally for different island_ids and summing their values.
      Use a set to check which ones have already been summed.

This is a O(N^2) time solution as we will go over each cell at least once (three times in the case of the islands).
The space is O(N^2) as the stack could contain all cells if the entire grid is an island.
"""

def max_island(grid):
    if len(grid) == 1:
        return 1

    N = len(grid)
    stack = []

    def find_size(row, col):
        if (not 0 <= row < N
            or not 0 <= col < N
            or grid[row][col] <= 0):
            return 0

        stack.append((row, col))
        grid[row][col] = -1

        return 1 + (find_size(row + 1, col)
                    + find_size(row - 1, col)
                    + find_size(row, col + 1)
                    + find_size(row, col - 1))

    island_id = 1
    max_size = 0
    for row in range(N):
        for col in range(N):
            if (type(grid[row][col]) == tuple or not grid[row][col]):
                continue

            island_size = find_size(row, col)
            max_size = max(max_size, island_size)

            while stack:
                curr_row, curr_col = stack.pop()

                grid[curr_row][curr_col] = (island_id, island_size)

            island_id += 1

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for row in range(N):
        for col in range(N):
            if grid[row][col]:
                continue

            added = set()
            size = 0
            for row_inc, col_inc in directions:
                if (not 0 <= row + row_inc < N
                    or not 0 <= col + col_inc < N):
                    continue

                adj_cell = grid[row + row_inc][col + col_inc]
                if adj_cell and not adj_cell[0] in added:
                    added.add(adj_cell[0])
                    size += adj_cell[1]

            max_size = max(max_size, size + 1)

    return max_size






        
