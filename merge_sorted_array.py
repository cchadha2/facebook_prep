"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


 This is the merge step of merge sort and will take O(m + n) time and O(m + n) space for an auxiliary array.

 Approach:
    - Auxiliary array that is a copy of nums1 (the larger array)
    - 2 pointers at start of nums1 and nums2
    - Iteratively take the smaller of the two values and fill into nums1

Example:
    - nums1 = [1, 4, 5, 0, 0, 0]
    - nums2 = [2, 3, 6]
    - output = [1, 2, 3, 4, 5, 6]


Follow up:
    - Can you do this in O(1) time?

If we iterate in reverse over nums2 and nums1 and fill in the back of nums1 as we go, we'd get the same result.
"""

def merge(nums1, nums2):

    aux = nums1.copy()
    n = len(nums2)
    m = len(nums1) - n

    idx = p1 = p2 = 0
    while p1 < m and p2 < n:

        if aux[p1] <= nums2[p2]:
            nums1[idx] = aux[p1]
            p1 += 1
        else:
            nums1[idx] = nums2[p2]
            p2 += 1

        idx += 1

    while idx < len(nums1) and p1 < m:
        nums1[idx] = aux[p1]
        idx += 1
        p1 += 1

    while idx < len(nums1) and p2 < n:
        nums1[idx] = nums2[p2]
        idx += 1
        p2 += 1

    return nums1


def merge(nums1, nums2):

    n = len(nums2)
    m = len(nums1) - n

    p1 = m - 1
    p2 = n - 1
    idx = len(nums1) - 1

    while idx >= 0 and p1 >= 0 and p2 >= 0:

        if nums1[p1] >= nums2[p2]:
            nums1[idx] = nums1[p1]
            p1 -= 1
        else:
            nums1[idx] = nums2[p2]
            p2 -= 1

        idx -= 1


    while idx >= 0 and p1 >= 0:
        nums1[idx] = nums1[p1]
        idx -= 1
        p1 -= 1

    while idx >= 0 and p2 >= 0:
        nums1[idx] = nums2[p2]
        idx -= 1
        p2 -= 1

    return nums1
