class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        checked_nums = set()

        # O(N) time and space for iteration and space for unique nums where N
        # is number of nums in nums.
        maximum_length = 0
        for num in nums:
            curr_length = 1

            if num in checked_nums:
                continue

            checked_nums.add(num)

            curr = num + 1
            # This loop and outer loop together can only ever by O(N) time
            # due to the checked_nums set.
            while curr in unique_nums:
                checked_nums.add(curr)
                curr += 1
                curr_length += 1

            maximum_length = max(maximum_length, curr_length)

        return maximum_length
