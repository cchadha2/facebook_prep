"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

x = b - a

=> (b - a) // k = n

Example 1:

Input: nums = [23,2,4,6,7], k = 6
sums = [23, 25, 29, 35, 42]

Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
sums = [23, 25, 31, 35, 42]

Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false


Input: nums = [23,4,8,6,7], k = 6
sums = [23, 27, 35, 41, 48]



Approach:
    - For any two sums at least one index away from each other, if a % k == b % k, then they will sum up to a multiple of k

"""


def continuous_sum(nums, k):

    sums = {}
    curr = 0

    for idx, num in enumerate(nums):
        curr += num

        if idx > 0 and not curr % k:
            return True

        # Only care about leftmost sum.
        if not curr % k in sums:
            sums[curr % k] = idx
        elif idx - sums[curr % k] > 1:
            return True


    return False
