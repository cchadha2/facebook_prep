# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        """O(N) time for idx iteration and O(N) space at most if tree is unbalanced."""
        
        idx = 0
        
        def build_tree():
            nonlocal idx
            if idx >= len(s):
                return
            elif s[idx] == ")":
                idx += 1
                return
           
            if s[idx] == "(":
                idx += 1
                
            sign = 1
            if s[idx] == "-":
                sign = -1
                idx += 1
                
            curr = 0
            while idx < len(s) and s[idx].isdigit():
                curr = (curr * 10) + int(s[idx])
                idx += 1
                
            node = TreeNode(sign * curr)
            
            node.left = build_tree()
            
            if node.left:
                node.right = build_tree()
                
            if node.right:
                idx += 1
            
            return node   
       
        return build_tree()
            
