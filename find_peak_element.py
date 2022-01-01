"""
Find any peak element's index where a[i - 1] < a[i] > a[i + 1].

Can do this in O(N) time and O(1) space by simply iterating through the list.

Can we improve on O(N) time?

Example:

3 possible cases:

1. We have a mix of peaks and troughs:
nums = [1,3,2,3,6,7,4]

2. We have a strictly increasing array:
nums = [1,2,3,4,5,6,7]

3. We have a strictly decreasing array:
nums = [7,6,5,4,3,2,1]


Can we use binary search to find an element with smaller adjacent elements?
    - Since no two adjacent elements can be equal, There must be a peak somewhere in the array (since indices -1 and N are -inf).
    - Check both extreme indices for peaks so that we can check both sides of each index in binary search.
    - Start with middle index and do a binary search.
    - If there is a bigger number adjacent to the current index, go towards it. If there isn't, you've found a peak.
    - From the 3 cases above, we can see that if we follow the rising elements, we will always know there is at least 1 smaller element to the
      left of each element. If the elements continue to rise, there is a peak at the end. If they don't, there is a dip on the right as well
      as a dip on the left so we've found a peak.

"""


def peak_index(nums):
    if len(nums) == 1:
        return 0

    if nums[0] > nums[1]:
        return 0
    elif nums[-1] > nums[-2]:
        return len(nums) - 1

    for idx in range(1, len(nums) - 1):
        if nums[idx - 1] < nums[idx] > nums[idx + 1]:
            return idx



def peak_index(nums):
    if len(nums) == 1:
        return 0

    if nums[0] > nums[1]:
        return 0
    elif nums[-1] > nums[-2]:
        return len(nums) - 1

    lo, hi = 1, len(nums) - 2

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid - 1] > nums[mid]:
            hi = mid - 1
        elif nums[mid + 1] > nums[mid]:
            lo = mid + 1
        else:
            return mid
