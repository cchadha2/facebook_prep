"""
nums = [23,2,6,4,7], k = 6
sums = [23, 25, 31, 35, 42]


nums = [23,2,4,6,6], k = 7
sums = [23, 25, 29, 35, 41]

nums = [23,2,6,4,7], k = 13
sums = [23, 25, 31, 35, 42]
"""

def check_subarray_sum(nums, k):
    # Overall O(N^2) time and O(N) space.
    if len(nums) == 1:
        return False

    # O(N) time and space.
    seen = set()
    sums = nums.copy()
    for idx in range(1, len(sums)):
        sums[idx] += sums[idx - 1]

    # O(N^2) time taking inner and outer loops into account.
    for idx in range(1, len(sums)):
        if not nums[idx - 1] and not nums[idx]:
            return True

        if not sums[idx] % k:
            return True

        if idx >= 2:
            seen.add(sums[idx - 2])

        # O(N) time in worst case if k = 1.
        multiplier = 1
        while multiplier * k <= sums[idx]:
            if sums[idx] - (multiplier * k) in seen:
                return True

            multiplier += 1

    return False
