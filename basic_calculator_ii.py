"""
input = "34+ 2*2 /  4"
output = 35

Explanation:
    2 * 2 / 4 must be evaluated first and is equal to 1 (2 * 2 = 4; 4/4 = 1).
    Then, 34 + 1 = 35

Approach:
    - Iterate through the string from the left, ignoring any whitespace
    - If a number is encountered, add it to a current sum since we must get through all digits of a number to find its value
    - Keep track of the current operator as we iterate ("+", "-", etc.)
    - If an operator is encountered, depending on its type, we should either append to a stack or carry out multiplication or division (these take precendence) and update the operator.
    - Then sum all of the numbers on the stack (delaying the addition and subtraction operations in this way)

O(N) time for iteration and O(N) space for the stack where N is number of characters in the expression.

Follow up:
    - Can you do this with O(1) space?
"""


def evaluate_expression(s):

    stack = []
    operator = "+"
    curr = 0

    # Remove whitespace at the end of s to allow check on line 38 to work.
    s = s.rstrip()
    for idx, char in enumerate(s):
        if char == " ":
            continue

        if char.isdigit():
            curr = (curr * 10) + int(char)

        if not char.isdigit() or idx == len(s) - 1:
            if operator == "+":
                stack.append(curr)
            elif operator == "-":
                stack.append(-curr)
            elif operator == "*":
                stack[-1] *= curr
            else:
                if stack[-1] < 0:
                    stack[-1] = -(-stack[-1] // curr)
                else:
                    stack[-1] //= curr

            curr = 0
            operator = char

    return sum(stack)


def evaluate_expression(s):

    operator = "+"
    res = last_num = curr = 0

    s = s.rstrip()
    for idx, char in enumerate(s):
        if char == " ":
            continue

        if char.isdigit():
            curr = (curr * 10) + int(char)

        if not char.isdigit() or idx == len(s) - 1:
            if operator in "+-":
                res += last_num
                last_num = curr if operator == "+" else -curr
            elif operator == "*":
                curr *= last_num
                last_num = curr
            else:
                if last_num < 0:
                    curr = -(-last_num // curr)
                else:
                    curr = last_num // curr
                last_num = curr

            curr = 0
            operator = char

    return res + last_num
