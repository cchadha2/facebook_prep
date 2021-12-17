

def depth_sum(seq):

    # O(N) time where N is number of integers in flattened list.
    # O(depth) space. Depth can be 50 at most so could also be
    # considered O(1).
    def weighted_sum(seq, depth):
        curr = 0
        for elem in seq:
            if type(elem) == int:
                curr += elem * depth
            else:
                curr += weighted_sum(elem, depth + 1)

        return curr

    return weighted_sum(seq, 1)
