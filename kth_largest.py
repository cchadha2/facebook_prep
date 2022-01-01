"""
Naive: O(NlogN) time and O(N) space with sorting and indexing.

Better: O(Nlogk) time and O(k) space with heap solution.
"""
import heapq

def kth_largest(nums, k):

    heap = nums[:k]
    heapq.heapify(heap)

    for idx in range(k, len(nums)):
        heapq.heappushpop(heap, nums[idx])

    return heapq.heappop(heap)
    
