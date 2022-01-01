"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.



Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

sum(weights) = 55

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:

Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1


Constraints:
    - Can weights be non-empty? No
    - Can we have negative weights? No
    - Will days always be greater than or equal to 1? Yes
    - It may be impossible to load the ship

Approach:
    - Write a function to check if the ship can be loaded within days days given a certain capacity (O(N) time where N is the number of weights and O(1) space).
    - Binary search with this function to find the lowest possible capacity O(logD) => Can we take 1000 as a reasonable limit for the number of days? Up this to 500,000 for LC


O(NlogD) time and O(1) space with iterative binary search.
"""
from math import inf


def find_min_capacity(weights, days):

    def check_possible(capacity):

        curr_weight = curr_days = 0
        for weight in weights:
            if weight > capacity or curr_days >= days:
                return False

            if curr_weight + weight > capacity:
                curr_days += 1
                curr_weight = weight
            else:
                curr_weight += weight

        return curr_days < days

    start, end = 1, 500_000
    minimum_capacity = hi
    while start <= end:
        mid = (start + end) // 2

        if check_possible(mid):
            minimum_capacity = mid
            end = mid - 1
        else:
            start = mid + 1

    return minimum_capacity
