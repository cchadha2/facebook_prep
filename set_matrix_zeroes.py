class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        This is an O(MN) time and O(1) space solution.
        """
        m, n = len(matrix), len(matrix[0])
        col_zero = False
        for row in range(m):

            if not matrix[row][0]:
                col_zero = True
                matrix[row][0] = 0

            for col in range(1, n):
                if not matrix[row][col]:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

        if not matrix[0][0]:
            for col in range(1, n):
                matrix[0][col] = 0

        if col_zero:
            for row in range(m):
                matrix[row][0] = 0
