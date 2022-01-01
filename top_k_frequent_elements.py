"""
nums = [5,2,1,6,3,2]
k = 2

output = [2, 5] (or 2 and any other elem)

Approach:
    - Count frequencies of each element using a hashmap (O(N) time and space).
    - Sort the items based on their counts (O(NlogN) time and O(N) space for sort).
    - Return the top k elements (O(k) time and space).

Overall O(NlogN) time and O(N) space.


Below implementations actually improve on this approach in terms of time complexity.
"""
import heapq

from collections import Counter


def top_k_elems(nums, k):
    """most_common method actually uses a heap for k < N so this is O(k + Nlogk + klogk) = O(Nlogk) time.

       O(N) space for the counter.
    """
    return [num for num, count in Counter(nums).most_common(k)]


def top_k_elems(nums, k):
    """ O(Nlogk) time and O(N) space."""
    counter = {}

    # O(N) time and space.
    for num in nums:
        counter.setdefault(num, 0)
        counter[num] += 1

    # O(N) time and space.
    count_pairs = [(count, elem) for elem, count in counter.items()]

    # O(k) time and space.
    heap = count_pairs[:k]
    heapq.heapify(heap)

    # O(Nlogk) time.
    for idx in range(k, len(count_pairs)):
        heapq.heappushpop(heap, count_pairs[idx])

    # O(k) time and space.
    return [elem[1] for elem in heap]
    
