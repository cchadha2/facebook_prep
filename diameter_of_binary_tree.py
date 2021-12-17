import math


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def diameter(root):
    if not root:
        return 0


    maximum = (-math.inf, [])

    # O(N) time as it visits each node. O(N * diameter) in worst case
    # for path list creation.
    # Between O(logN) and O(N) space depending on if tree is balanced.
    def dfs(node):
        if not node:
            return 0, []

        left, l_path = dfs(node.left)

        right, r_path = dfs(node.right)

        nonlocal maximum

        path_count = left + right
        if path_count > maximum[0]:
            maximum = path_count, l_path + [node.val] + list(reversed(r_path))

        if left >= right:
            l_path.append(node.val)
            return 1 + left, l_path
        else:
            r_path.append(node.val)
            return 1 + right, r_path


    dfs(root)

    return maximum[0]


        
