
def expression_equals_target(nums, target):
    """O(N * 4^N) time and O(N) space overall."""

    # O(N) time and space where N is number of chars in expression.
    def calculate(num):

        stack = []
        curr = 0
        operator = "+"

        for idx, char in enumerate(num, start=1):

            if char.isdigit():
                curr = (curr * 10) + int(char)

            if not char.isdigit() or idx == len(num):
                if operator == "+":
                    stack.append(curr)
                elif operator == "-":
                    stack.append(-curr)
                else:
                    stack[-1] *= curr

                curr = 0
                operator = char

        return sum(stack)


    # O(N * 4^N) time as we need to create a new string for each call and there
    # are 4 calls at most for each build_outputs call. O(N) space for call stack.
    def build_outputs(idx, expression, leading_zero=False):
        if idx == len(num):
            if calculate(expression) == target:
                output.append(expression)

            return

        curr_zero = num[idx] == "0"

        build_outputs(idx + 1, "".join((expression, "+", num[idx])), curr_zero)
        build_outputs(idx + 1, "".join((expression, "-", num[idx])), curr_zero)
        build_outputs(idx + 1, "".join((expression, "*", num[idx])), curr_zero)
        if not leading_zero:
            build_outputs(idx + 1, "".join((expression, num[idx])))


    output = []
    build_outputs(1, num[0], num[0] == "0")
    return output

def expression_equals_target(nums, target):
    """O(N * 4^N) time and O(N) space overall."""
    
        # O(N * 4^N) and O(N) space for call stack.
        def build_expression(idx, prev, curr, value, exp):
            if idx == len(num):
                if value == target and curr == 0:
                    output.append("".join(exp[1:]))
                return

            curr = (curr * 10) + int(num[idx])
            str_curr = str(curr)

            # No leading zeroes.
            if curr > 0:
                build_expression(idx + 1, prev, curr, value, exp)

            exp.extend(("+", str_curr))
            build_expression(idx + 1, curr, 0, value + curr, exp)
            exp.pop()
            exp.pop()

            if exp:
                exp.extend(("-", str_curr))
                build_expression(idx + 1, -curr, 0, value - curr, exp)
                exp.pop()
                exp.pop()

                exp.extend(("*", str_curr))
                build_expression(idx + 1, prev*curr, 0,
                                 # Need to take away previously added prev.
                                 value - prev + (prev * curr), exp)
                exp.pop()
                exp.pop()

        output = []
        build_expression(0, 0, 0, 0, [])
        return output
