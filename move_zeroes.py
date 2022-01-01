"""
Approach:
    - Iterate through nums and keep track of current indices of each zero in a stack
    - Go through the stack (from the end) and swap the right-most non-zero element with the index popped

How do we keep track of the non-zero indices?

Example:
nums = [1, 0, 2, 3, 0, 0, 4, 5]
output = [1, 2, 3, 4, 5, 0, 0, 0]

stack = [1, 4, 5]
non-zero = len(nums) - 1 => While this is greater than the popped index and it is a zero element, reduce the index.
Then swap the elements

O(N) time and space solution for the stack and the iteration.

Coded solution is O(N^2) time and O(N) space for stack.

On first iteration, move the first zero forward until we hit another zero. Then begin swapping the head of the zeroes
group with the non-zero tail until all zeroes are at the end.
This followup is an O(N) time and O(1) space solution.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        stack = []
        for idx, num in enumerate(nums):
            if not num:
                stack.append(idx)

        if not stack:
            return

        while stack:
            zero_idx = stack.pop()
            non_zero_idx = zero_idx + 1

            while non_zero_idx < len(nums) and nums[non_zero_idx]:
                nums[zero_idx], nums[non_zero_idx] = nums[non_zero_idx], nums[zero_idx]
                non_zero_idx += 1
                zero_idx += 1

    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return

        zero_idx = None
        for idx, num in enumerate(nums):
            if not num:
                zero_idx = idx
                break

        if zero_idx is None:
            return

        adj_idx = zero_idx + 1
        while adj_idx < len(nums) and nums[adj_idx]:
            nums[zero_idx], nums[adj_idx] = nums[adj_idx], nums[zero_idx]
            zero_idx += 1
            adj_idx += 1

        if adj_idx == len(nums):
            return

        while adj_idx < len(nums) and not nums[adj_idx]:
            adj_idx += 1

        if adj_idx == len(nums):
            return

        head = zero_idx
        tail = adj_idx
        while tail < len(nums):
            nums[head], nums[tail] = nums[tail], nums[head]

            head += 1
            while tail < len(nums) and not nums[tail]:
                tail += 1








        
