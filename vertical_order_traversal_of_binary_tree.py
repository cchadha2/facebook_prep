import math

import heapq

from collections import defaultdict


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_traversal(root):
    if not root:
        return []

    columns = defaultdict(list)

    min_column = math.inf

    # O(Nlogk) time where N is the number of nodes
    # and k is number of elements in that column.
    # Between O(logN) and O(N) space depending on
    # whether the tree is balanced and O(N) space for columns.
    def inorder(node, column, depth):
        if not node:
            return

        nonlocal min_column
        min_column = min(min_column, column)

        inorder(node.left, column - 1, depth + 1)

        heapq.heappush(columns[column], (depth, node.val))

        inorder(node.right, column + 1, depth + 1)


    # column = {-2: [(2, 4)], -1: [(1, 2)], 0: [(0, 1), (2, 5), (2, 6)], 1: [(1, 3)], 2: [(2, 7)]}
    inorder(root, 0, 0)

    # O(N) space where N is number of nodes.
    output = []
    # O(c * klogk) time where c is number of columns and k is number of elements in column.
    while min_column in columns:

        column = []
        # O(klogk) time where k is number of elements in column.
        for _ in range(len(columns[min_column])):
            column.append(heapq.heappop(columns[min_column])[1])

        output.append(column)

        min_column += 1

    # O(N * logk + c * klogk) time and O(N) space.
    # = O((N + ck)logk) time and O(N) space.
    # but ck = N so O(Nlogk) time.
    return output




    
