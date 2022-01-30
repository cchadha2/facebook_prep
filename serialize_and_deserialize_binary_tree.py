"""O(N) time and space solution."""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def level_order():
            queue = deque()
            queue.append(root)
            
            while queue:
                node = queue.popleft()
                
                if node:
                    yield str(node.val)
                
                    queue.append(node.left)
                    
                    queue.append(node.right)
                else:
                    yield "N" 
                    
       
        return ",".join(level_order()).rstrip(",N")
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        
        # Level order string with any trailing Ns stripped:
        # 1,2,3,N,N,4,5,N,N,N,N -> 1,2,3,N,N,4,5
        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue = deque()
        queue.append(root)
        idx = 1
        
        while idx < len(data):
            node = queue.popleft()
            
            if data[idx] != "N":
                node.left = TreeNode(int(data[idx]))
                queue.append(node.left)
                
            idx += 1
            if idx < len(data) and data[idx] != "N":
                node.right = TreeNode(int(data[idx]))
                queue.append(node.right)
                
            idx += 1
            
        return root
