
def remove_invalid_parens(s: str): -> list
    valid_expressions = set()
    min_removed = inf

    # O(2^N) time for worst case of all open parentheses.
    # This will not be a valid answer so won't need to add time
    # for building expression on line 15. O(N) space for expr and call stack.
    def remaining(idx, left, right, expr, removed):
        if idx == len(s):

            nonlocal min_removed
            if left == right and removed <= min_removed:

                expr = "".join(expr)
                if removed < min_removed:
                    nonlocal valid_expressions
                    valid_expressions = set()
                    min_removed = removed

                valid_expressions.add(expr)

            return

        if not s[idx] in "()":
            expr.append(s[idx])
            remaining(idx + 1, left, right,
                      expr, removed)
            expr.pop()
        else:
            # Remove current char.
            remaining(idx + 1, left, right,
                      expr, removed + 1)

            if s[idx] == "(":
                expr.append(s[idx])
                remaining(idx + 1, left + 1, right,
                          expr, removed)
                expr.pop()
            elif right < left:
                expr.append(s[idx])
                remaining(idx + 1, left, right + 1,
                          expr, removed)
                expr.pop()

    remaining(0, 0, 0, [], 0)
    return list(valid_expressions)

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
