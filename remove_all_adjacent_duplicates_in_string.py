"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.



Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"


"aaaaa"
output = "a"


Use a stack and iterate over the string from left to right. If the current char is a duplicate of what's on the stack, pop and continue.
Otherwise if the stack is empty or we don't have a duplicate, append to the stack.

Follow up:
    - Can we do this in O(1) space? -> Nah
"""


def dupe_removal(s):
    """Overall O(N) time and space where N is number of chars in s."""

    # O(N) space.
    stack = []
    # O(N) time.
    for char in s:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()

    # O(N) time and space.
    return "".join(stack)
