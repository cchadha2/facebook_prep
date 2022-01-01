"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

                -10
               /   \
              9     20
                   /  \
                  15   7
                 /
                -4

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

[15] = 15

Approach
    - Inorder traversal through the tree
    - Find maximum path sum through each node
    - Return the maximum path sum to the parent node
    - Maximum = max_left + node.val + max_right
    - Keep a global maximum outside scope of inner function
"""
from math import inf

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    """ O(N) time where N is the number of nodes.

    O(logN) and O(N) space depending on if tree is balanced or not
    """

    max_sum = -inf

    def post_order(node):
        if not node:
            return 0

        left = max(post_order(node.left), 0)
        right = max(post_order(node.right), 0)

        nonlocal max_sum
        max_sum = max(max_sum, left + node.val + right)

        return max(left, right) + node.val

    post_order(root)

    return max_sum
