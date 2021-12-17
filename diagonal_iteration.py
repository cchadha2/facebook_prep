"""
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

output = [1, 2, 4, 7, 5, 3, 6, 8, 9]
order = (0,0), (0, 1), (1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (2, 1), (2, 2)

Go along top row and then right most column and do alternating diagonal and anti-diagonal iterations.

mat = [[2,5],
       [8,4],
       [0,-1]]

mat = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

output = [1, 2, 5, 9, 6, 3, 4, 7, 10, 13, 14, 11, 8, 12, 15, 16]
"""


def diagonal_iteration(mat):
    """ Overall O(NM) as we're visiting each element once and O(1) space. """

    m, n = len(mat), len(mat[0])

    # O(M + N) time and O(1) space.
    def diagonal(row, col):
        # Row - 1, Col + 1 at each step.
        increment = min(m - 1 - row, col)
        curr_row, curr_col = row + increment, col - increment

        while curr_row >= 0 and curr_col < n:
            yield mat[curr_row][curr_col]
            curr_row -= 1
            curr_col += 1

    # O(M + N) time and O(1) space.
    def anti_diagonal(row, col):
        # Row + 1, Col - 1 at each step.
        increment = min(row, n - 1 - col)
        curr_row, curr_col = row - increment, col + increment

        while curr_row < m and curr_col >= 0:
            yield mat[curr_row][curr_col]
            curr_row += 1
            curr_col -= 1

    output = []
    diagonal_end = 0
    for col in range(n):
        if not col % 2:
            output.extend(diagonal(0, col))
            if col == n - 1:
                diagonal_end = 1
        else:
            output.extend(anti_diagonal(0, col))

    for row in range(1, m):
        if not diagonal_end % 2:
            output.extend(diagonal(row, n - 1))
        else:
            output.extend(anti_diagonal(row, n - 1))

        diagonal_end += 1

    return output
