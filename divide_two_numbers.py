class Solution:

    def __init__(self):
        self.positive = True

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend < 0 and divisor < 0:
            return self.divide(-dividend, -divisor)
        elif dividend < 0:
            self.positive = False
            return -self.divide(-dividend, divisor)
        elif divisor < 0:
            self.positive = False
            return -self.divide(dividend, -divisor)
        elif dividend == divisor:
            return 1
        elif divisor == 1:
            res = dividend
        else:
            res = 0
            # O(log^2(N)) time in total and O(1) space.
            while dividend >= divisor:

                prev_divisor = curr_divisor = divisor
                to_add = 0
                while dividend - curr_divisor >= 0:
                    prev_divisor = curr_divisor
                    curr_divisor += curr_divisor
                    to_add += max(1, to_add)

                dividend -= prev_divisor
                res += to_add


        return min(res, (2**31) - 1) if self.positive else min(res, 2**31)
