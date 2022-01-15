"""
This can be done recursively in O(2^N) time and O(N) space where N is the Nth
term which we are looking for.

Caching results will lead to an O(N) time and space solution.

Doing it iteratively leads to an O(N) time and O(1) space solution.
"""
from functools import cache


@cache
def fib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(15))

def fib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1

    prev, curr = 0, 1
    counter = 2
    while counter < n:
        next_val = prev + curr

        prev = curr
        curr = next_val
        counter += 1

    return curr

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(15))
