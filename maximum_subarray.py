from itertools import islice

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(N) time and O(1) space.
        maximum = curr = nums[0]
        for num in islice(nums, 1, None):
            curr = max(0, curr) + num
            maximum = max(maximum, curr)
            
        return maximum
            
