class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        O(N^2) time and O(1) space where matrix is NxN size.
        """

        def rotate_layer(start, end):
            if start >= end:
                return

            step = 0
            while start + step < end:
                temp = matrix[start][start + step]
                matrix[start][start + step] = matrix[end - step][start]
                matrix[end - step][start] = matrix[end][end - step]
                matrix[end][end - step] = matrix[start + step][end]
                matrix[start + step][end] = temp

                step += 1


        start, end = 0, len(matrix) - 1
        while start < end:
            rotate_layer(start, end)
            start += 1
            end -= 1
