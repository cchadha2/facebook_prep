"""
2 approaches:

1. DFS through tree, keeping track of depth as we proceed and maintaining a list of max values at each depth as we go.
2. BFS to traverse through each level iteratively and adding the maximum to an output list when the depth changes

Both are O(N) time but the second approach will be more performant as it is iterative and has at most O(row) extra space for the queue.
The first approach can have anywhere between O(logN) and O(N) space complexity depending on if the tree is balanced or not.
"""
from collections import deque

from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append((0, root))
        curr = 0
        row_max = -inf

        output = []
        while queue:
            depth, node = queue.popleft()

            if depth != curr:
                output.append(row_max)
                row_max = -inf
                curr = depth

            row_max = max(row_max, node.val)

            if node.left:
                queue.append((depth + 1, node.left))
            if node.right:
                queue.append((depth + 1, node.right))

        output.append(row_max)
        return output

            
