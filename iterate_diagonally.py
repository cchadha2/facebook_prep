grid = [list(range(start, start + 5)) for start in range(0, 20, 5)]

def print_grid(grid):
    for row in grid:
            print(row)

print_grid(grid)


def iterate_diagonal(row, col):
    decrement = min(row, col)
    start_row, start_col = row - decrement, col - decrement
    while start_row < len(grid) and start_col < len(grid[0]):
            print(grid[start_row][start_col])
            start_row += 1
            start_col += 1

iterate_diagonal(2, 3)

def iterate_anti_diagonal(row, col):
    increment = min(len(grid[0]) - 1 - col, row)
    curr_row, curr_col = row - increment, col + increment
    while curr_row < len(grid) and curr_col >= 0:
            print(grid[curr_row][curr_col])
            curr_row += 1
            curr_col -= 1

iterate_anti_diagonal(2, 3)
