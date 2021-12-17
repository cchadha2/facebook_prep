"""
weights = [1,2,3,1,1], days = 4

Given capacity of 2, is it possible to ship all packages within 4 days?

Answer:
    - Day 1 => Take 1 and ship
    - Day 2 => Take 2 and ship
    - Day 3 => Cannot take 3

    Therefore not possible

Capacity of 3?

Answer:
    - Day 1 => Take 1 and 2 and ship
    - Day 2 => Take 3 and ship
    - Day 3 => Take 1 and 1 and ship

    Therefore possible
"""
from math import inf


def min_weight(weights, days):

    # O(N) time where N is number of packages.
    def check_possible(capacity):
        curr_days = 0
        curr_sum = 0
        for weight in weights:

            if curr_sum > capacity or curr_days >= days:
                return False

            if curr_sum + weight > capacity:
                curr_sum = weight
                curr_days += 1
            else:
                curr_sum += weight

        return curr_sum <= capacity and curr_days + 1 <= days

    # O(NlogC) time where C is max possible capacity.
    # O(1) space.
    lo, hi = 0, ((5 * 10**4) * 500)
    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2

        if check_possible(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return ans
        
