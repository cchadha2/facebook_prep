"""

buildings = [1, 4, 2, 3]
output = [1, 3]

Approaches:
    - Iterate from the right and use a queue to appendleft the index of a building with an ocean view (O(N) time and O(N) space for queue).
    - Iterate from the right and add (height, idx) pairs to an array, then sort array and transform to only indices. (O(NlogN) time and O(N) space).
    - Iterate from the right and add (height, idx) pairs to a heap. Then create another array with heapsort contents (O(NlogN) time and O(N) space).

First solution is best, let's go with that.

Follow up:
    - If we have an ocean view on both sides, how do we find the buildings that have an ocean view in one pass?

Example:

buildings = [1, 4, 4, 2, 2, 3, 1]
output = [0, 6, 5, 1, 2]

Approach:
    - Use two pointers to go from the left and right inwards, simultaneously while tracking the max height on the left and right
    - The building has an ocean view if it is > the left or right max. If it does, mark it as None so the opposing sweep won't check it.
    - At each left or right index, check if there is a value and it is greater than the current seen max from the respective direction.
    - Add the buildings with oceans views to an array as (height, idx). Then sort.

O(NlogN) time (for sort) and O(N) space solution
"""
from collections import deque

from math import inf


def buildings_with_a_view(heights):
    if len(heights) == 1:
        return [0]

    queue = deque()

    maximum = -inf
    for idx in range(len(heights) - 1, -1 , -1):
        if heights[idx] > maximum:
            maximum = heights[idx]
            queue.appendleft(idx)

    return list(queue)


def buildings_with_two_views(heights):

    start, end = 0, len(heights) - 1
    ans = []

    left_max = right_max = -inf
    while start < len(heights):
        if start == end:
            if heights[start] > left_max or heights[start] > right_max:
                ans.append((heights[start], start))

        if heights[start] is not None and heights[start] > left_max:
            left_max = heights[start]
            ans.append((heights[start], start))
            heights[start] = None

        if heights[end] is not None and heights[end] > right_max:
            right_max = heights[end]
            ans.append((heights[end], end))
            heights[end] = None

        start += 1
        end -= 1

    ans.sort()
    return [idx for height, idx in ans]

buildings = [1, 4, 4, 2, 2, 3, 1]
output = [0, 6, 5, 1, 2]
print(buildings_with_two_views(buildings) == output)
    
