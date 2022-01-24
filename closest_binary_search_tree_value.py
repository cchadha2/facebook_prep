import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        heap = []
        
        # O(Nlogk) time and O(N + k) space for call stack and heap.
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            value = (-abs(node.val - target), node.val)
            if len(heap) == k:
                heapq.heappushpop(heap, value)
            else:
                heapq.heappush(heap, value)
        
            inorder(node.right)
        
        inorder(root)
        # O(k) time and space.
        return [heap.pop()[1] for _ in range(len(heap))]
