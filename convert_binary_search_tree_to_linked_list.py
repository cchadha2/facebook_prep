"""

                9
               / \
              5   10
             / \
            1   7
               /
              6

    1 <-> 5 <-> 6 <-> 7 <-> 9 <-> 10 <-> 1

"""
import operator

from math import inf

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_linked_list(root):
    if not root:
        return

    minimum = Node(inf)
    maximum = Node(-inf)

    # O(N) time as each node is visited.
    # Between O(logN) and O(N) space depending on if tree is balanced.
    def post_order(node):
        if not node:
            return minimum, maximum

        left_min, left_max = post_order(node.left)
        right_min, right_max = post_order(node.right)

        node.left = left_max
        left_max.right = node

        node.right = right_min
        right_min.left = node

        # Minimum and maximum of subtree.
        return (min(left_min, right_min, node, key=operator.attrgetter("val")),
                max(left_max, right_max, node, key=operator.attrgetter("val")))


    minimum, maximum = post_order(root)
    minimum.left = maximum
    maximum.right = minimum

    return minimum





    
