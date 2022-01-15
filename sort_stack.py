"""
Sort a stack with an additional temporary stack, such that the smallest items are on the top.

Example [4, 2, 5, 9, 1] -> [9, 5, 4, 2, 1]

1. [1] -> [1]
2. [2, 1] -> [2, 1]
3. [1, 2] -> [2, 1]
4. [] -> []


Approach:
    - Look at top of additional stack and stack to be sorted.
    - if additional stack is empty, push top of stack to additional stack
    - Otherwise, if top of additional stack <= top of stack, push top of stack
      to additional stack.
    - if it's the other way around, pop from both stacks and push top of stack
      to additional stack and then push item popped from additional stack back in.
      Keep popping from additional stack and pushing to original stack until we find
      an element that is greater than the popped item from the original stack or additional
      stack is empty.
    - Repeat until stack is appended and then push all items from additional stack
      back to original stack

"""

def sort_stack(stack):
    if not stack:
        return stack

    for idx in range(len(stack) - 1):
        if not stack[idx] >= stack[idx + 1]:
            break
    else:
        return stack

    # O(N) space.
    temp = []

    # O(N^2) time at worst and O(1) space.
    while stack:
        if not temp or temp[-1] <= stack[-1]:
            temp.append(stack.pop())
            continue

        elem = stack.pop()
        while temp and temp[-1] > elem:
            stack.append(temp.pop())

        temp.append(elem)

    # O(N) time and O(1) space.
    while temp:
        stack.append(temp.pop())

    return stack

print(sort_stack([4, 2, 5, 9, 1]))
print(sort_stack([1]))
print(sort_stack([2, 1]))
print(sort_stack([1, 2]))
print(sort_stack([]))
