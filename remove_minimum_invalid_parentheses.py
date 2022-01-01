"""

Since we are only looking to remove ANY invalid parentheses, we should discard ones that throw off the balance of left vs right parentheses as we go.

Start with the left side and remove any stray closing brackets and repeat with the right side for any stray opening brackets. This will be the minimum number of invalid parentheses removed by definition.

O(N) time for iterations and O(N) space for a queue needed to keep the characters in order as we check them from both sides.

Example:

s = "())()((a)"
output = "()()(a)"

Explanation:

Removed two parentheses after checking from left and right sides. This is the minimum to be removed.
"""
from collections import deque


def min_remove(s):

    queue = deque()
    left = right = 0

    for char in s:
        if char == "(":
            left += 1
        elif char == ")":
            if right + 1 > left:
                continue

            right += 1

        queue.append(char)

    to_check = len(queue)
    left = right = 0
    for _ in range(to_check):
        char = queue.pop()

        if char == ")":
            right += 1
        elif char == "(":
            if left + 1 > right:
                continue

            left += 1

        queue.appendleft(char)

    return "".join(queue)

    
