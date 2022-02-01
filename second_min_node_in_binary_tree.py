# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
        
        6
       / \
      8   6
     / \ 
    8  12
       / \
      12  14

ans = 8

"""
from math import inf


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        """O(N) time and space solution."""
        
        minimum = root.val
        second_min = inf
       
        def traverse_tree(node):
            if not node:
                return
            
            nonlocal second_min
            if node.left:
                if node.left.val != minimum:
                    second_min = min(node.left.val, second_min)
                else:
                    traverse_tree(node.left)
                    
                if node.right.val != minimum:
                    second_min = min(node.right.val, second_min)
                else:
                    traverse_tree(node.right)
                           
        traverse_tree(root)
        return second_min if second_min != inf else -1
                
            
            
