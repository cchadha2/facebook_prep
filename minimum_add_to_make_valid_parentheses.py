"""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

Constraints:
    - s only consists of "(" and ")" chars
    - No empty string? True

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3


input s = ")))"
output = 3


Approach:
    - Number of opening and closing parentheses should be equal
    - Iterate through s and maintain a stack of parentheses
    - If we are at an opening parentheses, append it to the stack
    - If we're at a closing parentheses and the last element on the stack is an opening one, pop from the stack.
      Otherwise, if the stack is empty or the last element is also a closing parentheses, append to the stack.

We will be left with the number of unmatched parentheses in this way and the answer is simply the length of the stack.

O(N) time for iteration through the string and potentially O(N) space for the stack in the worst case of all opening parentheses.
"""


def minimum_add_to_make_valid_parentheses(s):

    stack = []

    for char in s:
        if char == ")" and stack and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(char)

    return len(stack)

def minimum_add_to_make_valid_parentheses(s):
    """O(N) time and O(1) space optimization."""

    num_added = open_unmatched = 0
    for char in s:
        open_unmatched += 1 if char == "(" else -1
        # If we have more closing than opening brackets, add an opening bracket.
        if open_unmatched == -1:
            open_unmatched += 1
            num_added += 1

    return num_added + open_unmatched
