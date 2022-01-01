"""
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]. Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below.

rotLeft has the following parameter(s):

int a[n]: the array to rotate
int d: the number of rotations
Returns

int a'[n]: the rotated array
Input Format

The first line contains two space-separated integers  and , the size of  and the number of left rotations.
The second line contains  space-separated integers, each an .

Constraints

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4

Follow up:
    - Do this in-place?

Can do it with 3 stacks instead?

"""
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    # O(N) time and space.
    queue = deque(a)

    # O(d) time.
    for _ in range(d):
        queue.append(queue.popleft())

    return queue


def rotLeft(a, d):
    d %= len(a)

    # a =[1, 2, 3, 4, 5] and d = 3
    second_stack, third_stack = [], []

    # a =[1, 2, 3] and d = 3
    # 2 = [5, 4]
    for _ in range(len(a) - d):
        second_stack.append(a.pop())

    # a =[] and d = 3
    # 2 = [5, 4]
    # 3 = [3, 2, 1]
    while a:
        third_stack.append(a.pop())

    # a =[4, 5] and d = 3
    # 2 = []
    # 3 = [3, 2, 1]
    while second_stack:
        a.append(second_stack.pop())

    while third_stack:
        a.append(third_stack.pop())

    return a



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
