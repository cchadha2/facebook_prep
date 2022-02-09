import random

class Solution:

    def __init__(self, nums: List[int]):
        """O(N) time and space."""
        self.table = {}
        for idx, num in enumerate(nums):
            self.table.setdefault(num, []).append(idx)
            

    def pick(self, target: int) -> int:
        """O(1) time."""
        return random.choice(self.table[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


class Solution:

    def __init__(self, nums: List[int]):
        """O(1) time and space."""
        self.nums = nums

    def pick(self, target: int) -> int:
        """O(N) time and O(1) space using reservoir sampling."""
        target_idx = 0
        count = 0
        
        for idx, num in enumerate(self.nums):
            if num == target:
                count += 1
                
                if random.randint(1, count) == count:
                    target_idx = idx
                    
        return target_idx
