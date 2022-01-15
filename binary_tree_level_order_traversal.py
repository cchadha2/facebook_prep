from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Do a BFS with a queue and keep track of depth. O(N) time where N is number of nodes.
# O(2^max_depth) space for queue.
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return

        queue = deque()
        queue.append((0, root))
        depth = 0
        row = []
        output = []

        while queue:
            curr_depth, node = queue.popleft()

            if curr_depth == depth:
                row.append(node.val)
            else:
                output.append(row)
                depth = curr_depth
                row = [node.val]

            if node.left:
                queue.append((curr_depth + 1, node.left))
            if node.right:
                queue.append((curr_depth + 1, node.right))


        output.append(row)
        return output
