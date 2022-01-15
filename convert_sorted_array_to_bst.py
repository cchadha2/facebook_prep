# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # O(N) time to visit each num and O(logN) space as we're dividing
        # nums by 2 each time.
        def build_tree(start, end):
            if start > end:
                return
            elif start == end:
                return TreeNode(nums[start])

            mid = (start + end) // 2
            return TreeNode(nums[mid],
                            left=build_tree(start, mid - 1),
                            right=build_tree(mid + 1, end))

        return build_tree(0, len(nums) - 1)
