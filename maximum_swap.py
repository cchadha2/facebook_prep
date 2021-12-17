"""

Example = 837284

Answer = 887234

Method:
    - Split numbers into a list: [8, 3, 7, 2, 8, 4] (O(N) time and O(N) space)
    - From the end of the list, find the maximum idx to swap. Simultaneously find the leftmost number to swap with the max idx as we go (O(N) time).
    - Swap the appropriate integers (O(1) time)

Overall O(N) time and space for order list, traversal, and cast to int.
"""


def maximum_swap(num):
    order = list(str(num))

    lo = hi = max_idx = len(order) - 1
    for idx in range(len(order) - 1, -1, -1):
        if order[idx] > order[max_idx]:
            max_idx = idx
        elif order[idx] < order[max_idx]:
            lo, hi = idx, max_idx

    order[lo], order[hi] = order[hi], order[lo]

    return int("".join(order))


    
