from itertools import islice

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        overall_max = curr_max = curr_min = nums[0]
        
        # O(N) time and O(1) space.
        for num in islice(nums, 1, None):
            curr_max, curr_min = (max(num, curr_max * num, curr_min * num),
                                  min(num, curr_max * num, curr_min * num))
            
            overall_max = max(overall_max, curr_max)
            
        return overall_max
