class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        """O(N) time and space solution."""
        nums = [x*x*a + x*b + c for x in nums]
        ans = [0] * len(nums)
        
        lo, hi = 0, len(nums) - 1
        idx, dec = (lo, 1) if a < 0 else (hi, -1)
        while lo <= hi:
            left, right = nums[lo], nums[hi]
            
            if a >= 0:
                if left > right:
                    ans[idx] = left
                    lo += 1
                else:
                    ans[idx] = right
                    hi -= 1
            else:
                if left > right:
                    ans[idx] = right
                    hi -= 1
                else:
                    ans[idx] = left
                    lo += 1
                    
            idx += dec
                    
        return ans
        
