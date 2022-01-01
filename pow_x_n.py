"""
Note that x^(-2) = 1 / x^2

Example:

    3^4
= 3 * 3 * 3 * 3
= 3^2 * 3^2
= 9 * 9
= 81

    2^10
= 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
= pow(2, 5) * pow(2, 5)
= pow(2, 2) * pow(2, 2) * pow(2, 2) * pow(2, 2)
= pow(2, 1) * pow(2, 1) * pow(2, 1) * pow(2, 1) * pow(2, 1) * pow(2, 1) * pow(2, 1) * pow(2, 1)

Approaches
1. We can do this simply with `x**n` for a constant time and space solution.
2. Recursive solution where we have a base case of x^1 = x or x^0 = 1 and we multiply pow(x, n//2) * pow(x, n//2) * pow(x, n % 2)?


"""
from functools import cache


def pow(x, n):
    return x**n


def pow(x, n):
    """O(N) time and O(N) space solution"""
    if n < 0:
        return 1 / pow(x, n)
    if n == 1:
        return x

    return x * pow(x, n - 1)

@cache
def pow(x, n):
    """O(logN) time and O(logN) space solution (for cache and call stack)."""
    if n < 0:
        return 1 / pow(x, -n)
    if n == 1:
        return x
    elif n == 0:
        return 1

    return (pow(x, n // 2) * pow(x, n // 2)) * pow(x, n % 2)
