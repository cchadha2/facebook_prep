"""
intervals = [[2, 6], [15, 18], [8, 10], [1, 4]]
output = [[1, 10], [15, 18]]

There are 3 cases where an interval can overlap:
1. end_1 >= start_2 and start_1 < start_2:
   _____
      ______
2. end_1 >= start_2 and start_1 >= start_2:
    _____
   _______
3. start_1 >= start_2 and end_1 > end_2:
     _____
   _____

If we sort by the end times, we can avoid case 3 altogether and only deal
with case 1 and 2. We can do the same with the start times as well.

Facebook Follow-Up
Question: How do you add intervals and merge them for a large stream of intervals?

Inspired by https://leetcode.com/problems/merge-intervals/discuss/21452/Share-my-interval-tree-solution-no-sorting

"""
def merge_intervals(intervals):
    """ Sorting by ending times.

    O(NlogN) time and O(N) space at most.
    """


    # O(N) space at worst.
    res = []
    # O(NlogN) time where N is number of intervals.
    intervals.sort(key=lambda interval: interval[1])

    # O(N) time.
    while intervals:
        interval = intervals.pop()

        while intervals and intervals[-1][1] >= interval[0]:
            next_interval = intervals.pop()

            interval[0] = min(interval[0], next_interval[0])
            interval[1] = max(interval[1], next_interval[1])


        res.append(interval)

    # O(N) time and space.
    return res


def merge_intervals(intervals):
    """Sorting by the start times.

    O(NlogN) time and O(N) space at most.
    """


    # O(N) space at worst.
    res = []
    # O(NlogN) time where N is number of intervals.
    intervals.sort(key=lambda interval: interval[0])

    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])


    # O(N) time and space.
    return res
