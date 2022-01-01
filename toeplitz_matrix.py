"""
Starting from bottom left element and iterating towards top right, check that the diagonals from those elements all have the same value. i.e. go over all of first column, descending rows and then then all of the first row, ascending columns, and look for the diagonals from them.

This solution will be O(MN) time as each element is checked exactly once. O(1) extra space is required.

Follow up:
    - What if you could only get access to one row at a time?

Ans: There are a total of M + N - 1 diagonals in the matrix. If we create a list of M + N - 1 elements where we fill in the required element for each diagonal as we come across it, we can then check row by row if we meet the toepltiz matrix condition.

    - What if the matrix is so large that you can only load up a partial row at a time?

Ans: We can repeat a similar algorithm to the follow-up above, keeping track of the indices in the partial row as we go, as long as we have access to all of the parts of a single row in sequential order. Otherwise, we could not keep track of the indices as we go over rows.
"""


def toeplitz_matrix(mat):

    m, n = len(mat), len(mat[0])

    for row in range(m - 1, -1, -1):
        curr_row, curr_col = row, 0

        element = mat[curr_row][curr_col]

        while curr_row < m and curr_col < n:
            if not mat[curr_row][curr_col] == element:
                return False

            curr_row += 1
            curr_col += 1


    for col in range(1, n):
        curr_row, curr_col = 0, col

        element = mat[curr_row][curr_col]

        while curr_row < m and curr_col < n:
            if not mat[curr_row][curr_col] == element:
                return False

            curr_row += 1
            curr_col += 1

    return True

def toeplitz_matrix_followup(mat):

    m, n = len(mat), len(mat[0])
    elements = [None] * (m + n - 1)

    element_start = m - 1
    for row in mat:
        for idx, val in zip(range(element_start, element_start + n), row):
            if elements[idx] is None:
                elements[idx] = val
            elif elements[idx] != val:
                return False
        element_start -= 1

    return True


def toeplitz_matrix_followup_two(mat):

    m, n = len(mat), len(mat[0])
    elements = [None] * (m + n - 1)
    elem_start = m - 1

    for row in mat:
        start = 0
        curr_elem_start = elem_start
        while start < len(row):
            for idx, val in zip(range(curr_elem_start, curr_elem_start + n // 2),
                                row[start : start + n // 2]):

                if elements[idx] is None:
                    elements[idx] = val
                elif elements[idx] != val:
                    return False
            curr_elem_start += n // 2
            start += (n // 2) or 1

        curr_elem_start += n // 2
        elem_start -= 1

    return True
    
