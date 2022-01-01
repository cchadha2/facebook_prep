"""
height = [4,2,0,3,2,5]

output = 9

- Record max height from the left for each index
- Do the same for max height from the right
- contribution = min(left_max, right_max) - height

left = [4, 4, 4, 4, 4, 5]
right = [5, 5, 5, 5, 5, 5]

contribution = [0, 2, 4, 1, 2, 0]
res = 2 + 4 + 1 + 2
    = 9

O(N) time and space solution as we require N extra space for max array(s) and O(N) time to iterate over heights twice.
"""
from math import inf


def trapping_rain_water(height):

    left = [None] * len(height)

    maximum = -inf
    for idx in range(len(height)):
        maximum = max(maximum, height[idx])
        left[idx] = maximum

    res = 0
    maximum = -inf
    for idx in range(len(height) - 1, -1, -1):
        maximum = max(maximum, height[idx])

        res += min(maximum, left[idx]) - height[idx]

    return res
