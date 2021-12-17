"""
Input: order = "cbafg", s = "abcd"
Output: "cbad"
"""
from math import inf

def custom_sort(order, s):

    # O(1) time as there will always be 26 chars at most in order.
    start = ord("a")
    reverse_idx = [None] * 26
    for idx, char in enumerate(order):
        reverse_idx[ord(char) - start] = idx

    # O(1) time again as only 26 elements in reverse_idx.
    for idx, value in enumerate(reverse_idx):
        if value is None:
            reverse_idx[idx] = inf

    # O(SlogS) time and O(S) extra space for sorted list and new string.
    return "".join(sorted(s, key=lambda char: reverse_idx[ord(char) - start]))

# O(s) time and space optimized solution.
def custom_sort(order, s):
    counts = Counter(s)

    def gen_first_chars():
         for char in order:
            yield char * counts[char]
            counts[char] = 0

    counts_keys = list(counts.keys())
    return "".join(
        chain.from_iterable((
            gen_first_chars(),
            (char * counts[char] for char in counts_keys)
        ), )
    )
