"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

Constraints:
    - Empty root is not possible
    - Return a list of lists of integers for each column, sorted by the values and the lists are sorted by their column from left to right


Example:


                                6
                              /   \
                             5     2
                           /   \ /   \
                          4    3 1    7

output = [[4], [5], [1, 3, 6], [2], [7]]


Approach:
    - Do an inorder traversal of the tree (O(N) time and between O(logN) and O(N) space at worst).
    - Track the column and depth as we go and add values to a hashmap of columns: lists
    - The output will be the values of the hashmap, sorted internally
    - Also track the min and max column for easy iteration over the hashmap's keys

O(N + W*HlogH) time and O(N) space for the hashmap.
"""
from math import inf


def vertical_traverse(root):
    """Overall O(N + W*HlogH) time and O(N) space for hashmap."""

    columns = {}
    min_column = inf
    max_column = -inf

    # O(N) time and space for dfs and columns hashmap.
    def inorder(node, column, depth):
        if not node:
            return

        inorder(node.left, column - 1, depth + 1)

        nonlocal min_column, max_column
        min_column = min(column, min_column)
        max_column = max(column, max_column)

        columns.setdefault(column, []).append((depth, node.val))

        inorder(node.right, column + 1, depth + 1)


    inorder(root, 0, 0)

    output = []
    # O(W*HlogH) time and O(H) space for sort.
    for column in range(min_column, max_column + 1):
        columns[column].sort()
        for idx, pair in enumerate(columns[column]):
            depth, value = pair
            columns[column][idx] = value

        output.append(columns[column])


    return output
