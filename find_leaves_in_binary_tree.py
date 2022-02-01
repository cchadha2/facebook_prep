# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
        leaves = []
        
        def inorder(node):
            if not node:
                return
            
            left = inorder(node.left)
            
            if left:
                leaves.append(node.left.val)
                node.left = None
                
            right = inorder(node.right)
            
            if right:
                leaves.append(node.right.val)
                node.right = None
                
            return (left is None and right is None)
       
        # In worst case of completely unbalanced tree:
        # N nodes on first iter.
        # N - 1 nodes on second iter.
        # N - 2 nodes on third iter
        # ... 1 node on last iter.
        # => O(N^2) time (triangular sum) and O(N) space for call stack
        # (leaves array will always have less than N nodes).
        while root.left or root.right:
            inorder(root)
            
            output.append(leaves)
            leaves = []
            
        output.append([root.val])
            
        return output
            
                
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """O(N) time and space solution."""
        
        output = []
            
        def postorder(node):
            if not node:
                return -1
            
            left = postorder(node.left)
            right = postorder(node.right)
            
            curr_dist = max(left, right) + 1
            
            if len(output) == curr_dist:
                output.append([])
                
            output[curr_dist].append(node.val)
            return curr_dist
        
        postorder(root)
        return output
            
            
            
