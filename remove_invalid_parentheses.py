"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]


Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.


Approach:
    - Seems like a backtracking problem where we count the number of left and right parentheses we've added and ensure we don't have an imbalanced string
    - Find the minimum number of invalid left and right parentheses first by scanning string left to right and then right to left
    - Then recursively choose to add or remove open or closing parentheses as we move through s based on the number of left and right parentheses that we know we need to remove
    - When idx == len(s) append the results of the stack to the output list and pop from last call

O(2^N) time for recursion and O(N) space for stack where N is number of chars in s.
"""
from collections import deque


def remove_min_invalid(s):


    queue = deque()

    right_remove = left_remove = 0
    open_count = closed_count = 0
    for char in s:
        if char == "(":
            open_count += 1
        elif char == ")":
            if closed_count + 1 > open_count:
                right_remove += 1
                continue

            closed_count += 1

        queue.append(char)


    open_count = closed_count = 0
    N = len(queue)
    for _ in range(N):
        char = queue.pop()

        if char == ")":
            closed_count += 1
        elif char == "(":
            if open_count + 1 > closed_count:
                left_remove += 1
                continue

            open_count += 1


    stack = []
    output = set()

    def build_combinations(idx, stack, left_removed, right_removed, left, right):
        if idx == len(s):
            if (left == right
                and left_removed == left_remove
                and right_removed == right_remove):
                output.add("".join(stack))

            return

        # Keep the current char if it is a letter.
        if s[idx].isalpha():
            stack.append(s[idx])
            build_combinations(idx + 1, stack, left_removed, right_removed, left, right)
            stack.pop()
        else:
            if s[idx] == ")":
                # Discard the closing paren.
                if right_removed < right_remove:
                    build_combinations(idx + 1, stack, left_removed, right_removed + 1, left, right)

                if left > right:
                    # Keep the closing paren.
                    stack.append(s[idx])
                    build_combinations(idx + 1, stack, left_removed, right_removed, left, right + 1)
                    stack.pop()
            else:
                # Keep the opening paren.
                stack.append(s[idx])
                build_combinations(idx + 1, stack, left_removed, right_removed, left + 1, right)
                stack.pop()


                # Discard the opening paren.
                if left_removed < left_remove:
                    build_combinations(idx + 1, stack, left_removed + 1, right_removed, left, right)

    build_combinations(0, stack, 0, 0, 0, 0)
    return list(output)
      

def remove_invalid_parens(s: str): -> list
    """Overall O(2^N) time an O(N) space but fewer calls overall and less space"""
    # Count the number of misplaced left and right parens.
    # O(N) time and O(1) space.
    left = right = 0

    for char in s:
        if char == "(":
            left += 1
        elif char == ")":
            if left:
                left -= 1
            else:
                right += 1

    # O(2^N) calls at most (worst case with all left parentheses).
    # O(N) space for expr and call stack.
    def build_expression(idx, left_rem, right_rem, left_count, right_count, expr):
        if idx == len(s):
            if not left_rem and not right_rem:
                output.add("".join(expr))

            return

        char = s[idx]

        if not char in "()":
            expr.append(char)
            build_expression(idx + 1, left_rem, right_rem,
                             left_count, right_count, expr)
        else:
            if (char == "(" and left_rem)  or (char == ")" and right_rem):
                build_expression(idx + 1,
                                 left_rem - (char == "("),
                                 right_rem - (char == ")"),
                                 left_count, right_count, expr)

            expr.append(char)

            if char == "(":
                build_expression(idx + 1, left_rem, right_rem,
                                 left_count + 1, right_count, expr)
            elif right_count < left_count:
                build_expression(idx + 1, left_rem, right_rem,
                                 left_count, right_count + 1, expr)

        expr.pop()

    output = set()
    build_expression(0, left, right, 0, 0, [])
    return list(output)
