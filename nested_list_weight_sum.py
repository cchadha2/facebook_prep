"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

Constraints:
    - Can there be negative numbers? Yes
    - Can there be an empty list? No

Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.


Approach:
    - Iterate over elements of nestedList
    - If element is a list, recurse with depth + 1
    - Set that element's value to the sum of the nested list
    - Sum the entire list of integers after processing


O(N) time where N is number of integers in nestedList in total. O(D) space for call stack where D is max depth.
"""


def nested_sum(nestedList):

    def calculate_sum(seq, depth):

        value = 0
        for elem in seq:
            if type(elem) is list:
                value += calculate_sum(elem, depth + 1)
            else:
                value += elem * depth

        return value

    return calculate_sum(nestedList, 1)


inp = [[1,1],2,[1,1]]
expected = 10
print(nested_sum(inp) == expected)

inp = [0]
expected = 0
print(nested_sum(inp) == expected)

inp = [[1, 3], 4, [1, [2, [3, [4, [5, [6]]]]]]]
expected = 124
print(nested_sum(inp) == expected)
