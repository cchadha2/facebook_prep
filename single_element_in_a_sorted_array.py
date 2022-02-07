class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # O(N) time and O(1) space.
        curr = 0
        for num in nums:
            curr ^= num
            
        return curr
    
    
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # O(logN) time and O(1) space.
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            
            # If we know the previous number is the same as
            # current number and the range [lo, mid] contains
            # an odd number of terms, then the duplicate must be
            # in [lo, mid - 1]. Otherwise, the duplicate is in [mid + 1, hi].
            
            if not (0 < mid < len(nums) - 1):
                return nums[mid]
            
            if nums[mid] == nums[mid - 1]:
                if (mid + 1 - lo) % 2:
                    hi = mid - 2
                else:
                    lo = mid + 1
            elif nums[mid] == nums[mid + 1]:
                if (hi + 1 - mid) % 2:
                    lo = mid + 2
                else:
                    hi = mid - 1
            else:
                return nums[mid]
                
           
        
