"""
Objective: Given a number, find out whether its colorful or not.

Colorful Number: When in a given number, product of every digit of a sub-sequence are different. That number is called Colorful Number. See Example

Example:

Given Number : 3245
Output : Colorful
Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
this number is a colorful number, since product of every digit of a sub-sequence are different.
That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40

Given Number : 326
Output : Not Colorful.
326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12.

Questions:
    - Is a full sequence considered a sub sequence? Yes
    - Negative numbers possible? Yes
    - Single or two digit numbers possible? Yes

Approach:
    - For each digit, expand a window to the right to a max of N - 1 length
    - Keep track of products in a set as you expand
    - If any product already exists, it is not a colourful number

O(N^2) time and O(N) space.
"""


def colourful(num):
    if num < 0:
        return colourful(-num)

    str_num = str(num)
    if len(str_num) == 1:
        return "Colourful"

    n = len(str_num)
    seen = set()

    for start in range(n):
        end = start + 1
        product = int(str_num[start])

        if not product or product in seen:
            return "Not Colorful"

        seen.add(product)

        while end < n:
            product *= int(str_num[end])

            if product in seen:
                return "Not Colorful"

            seen.add(product)

            end += 1

    return "Colorful"

print(colourful(3245))
print(colourful(326))
print(colourful(-1))
print(colourful(10))
print(colourful(33333))
