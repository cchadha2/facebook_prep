"""
Approach:
    - Reduce the problem to two-sum where we find the complement index to the current index such that current + complement + k = 0
    - k in this instance will be each num of nums that we haven't previously seen
    - To do step 2, we should sort the array and maintain a pointer of the idx for the current and complement sums

Example:
    nums = [1, 2, -1, 3, 2, -3]
    sorted(nums) = [-3, -1, 1, 2, 2, 3]

output = [(-3, 1, 2)] -> ignore the next (-3, 1, 2) by advancing the pointer beyond like terms.

We should also break when we get to a k > 0 as there will be no numbers beyond that k which sum to 0.

This should be O(N^2) time and O(N) space for the hashset of complements.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        print(nums)

        output = []
        for k_idx, k in enumerate(nums):
            if k > 0:
                break
            elif k_idx and nums[k_idx - 1] == nums[k_idx]:
                continue

            seen = set()
            idx = k_idx + 1
            while idx < len(nums):

                curr = nums[idx]
                complement = -(curr + k)

                if complement in seen:
                    output.append([k, complement, curr])

                    while idx < len(nums) and nums[idx] == curr:
                        idx += 1
                else:
                    idx += 1

                seen.add(curr)

        return output

                
