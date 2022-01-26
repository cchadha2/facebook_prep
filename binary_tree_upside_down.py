# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
        2
       / \
      1   3


        1
       / \
      3   2


For each node, make its left child point to the node and the right child
on its left and right child pointers.

Do this level by level and then your new root will be the left most node overall.

O(N) time as we visit each node once and O(N) space at most for queue.
"""

from collections import deque


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        elif not root.left:
            return root
        
        
        node = root
        while node.left:
            node = node.left
            
        min_node = node
        
        
        queue = deque()
        queue.append((None, root, None))
        
        while queue:
            left_parent, node, right_sibling = queue.popleft()
            
            if node.left:
                queue.append((node, node.left, node.right))
            if node.right:
                queue.append((None, node.right, None))
                
            if left_parent:
                if left_parent.left is node:
                    left_parent.left = left_parent.right = None
                    
                node.right = left_parent
                node.left = right_sibling
                
            
                
                
        return min_node
        
