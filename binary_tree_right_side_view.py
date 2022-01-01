"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Constraints:
    - empty root? Yes it is possible
    - Balanced tree? Not necessarily
    - Ordered on depth, not on value? Yes


Example:

                7
               / \
              5   3
             /   / \
            2   4   8
           /   /
          1   9
           \
            10


Output = [7, 3, 8, 9, 10]

Approach:
    - Start at root and go towards the right, tracking depth as we go.
    - If current node's depth is greater than max depth, this node is visible from the right side

This is a DFS with an extra step to track depth => O(N) time and space solution.
"""
def right_side(root):
    if not root:
        return []

    max_depth = -1
    output = []

    def dfs(node, depth):
        if not node:
            return

        nonlocal max_depth
        if depth > max_depth:
            max_depth = depth
            output.append(node.val)

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)


    dfs(root, 0)
    return output


def right_side(root):
    if not root:
        return []

    max_depth = -1
    output = []
    stack = [(root, 0)]

    while stack:
        node, depth = stack.pop()

        if depth > max_depth:
            output.append(node.val)
            max_depth = depth

        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))

    return output
