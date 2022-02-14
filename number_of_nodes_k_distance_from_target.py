from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        output = []
        
        # Find parents of nodes in tree.
        stack = [(None, root)]
        while stack:
            parent, node = stack.pop()
            
            node.parent = parent
                
            if node.left:
                stack.append((node, node.left))
            if node.right:
                stack.append((node, node.right))
                
                
        # From target, find all nodes k distance away.
        queue = deque()
        queue.append((target, 0))
        visited = set()
        
        while queue:
            node, distance = queue.popleft()
            
            if distance == k:
                output.append(node.val)
            elif distance > k:
                break
            elif node.val in visited:
                continue
                
            visited.add(node.val)
            
            if node.left and not node.left.val in visited:
                queue.append((node.left, distance + 1))
            if node.right and not node.right.val in visited:
                queue.append((node.right, distance + 1))
            if node.parent and not node.parent.val in visited:
                queue.append((node.parent, distance + 1))
                
        return output
                
