"""
Negative numbers in the array so sliding window approach wouldn't work.
A prefix sums approach is the way to go.

Approach:
    - Track the total sum as we iterate
    - At each step, check if the sum's complement has already been seen where
      complement = curr - k
    - If it has, add count += seen[complement]
    - Increment seen[curr] by 1 (add it if it doesn't already
      exist in the hashmap)

This is an O(N) time and space solution as we iterate over all of the N nums and
maintain a hashmap that will contain at most N items.
"""

def subarray_sum(nums, k):

    seen = {}
    curr = count = 0

    for num in nums:
        curr += num

        if curr == k:
            count += 1

        complement = curr - k
        if complement in seen:
            count += seen[complement]

        seen.setdefault(curr, 0)
        seen[curr] += 1

    return count
