from collections import deque


def look_and_say(n):

    # O(S) time where S is number of chars in string.
    # O(num_groups) space where num_groups is number of groups in string.
    def increment(num=None):
        if num == "1":
            return "11"

        curr = None
        count = 0
        stack = []
        for idx in range(len(num)):
            if not curr:
                curr = num[idx]
                count += 1
            elif num[idx] != curr:
                stack.append((curr, count))
                curr = num[idx]
                count = 1
            else:
                count += 1

            if idx == len(num) - 1:
                stack.append((curr, count))

        return "".join(str(count) + curr for curr, count in stack)

    # O(NS) time and O(num_groups) space.
    curr = "1"
    for _ in range(n):
        print(curr)
        curr = increment(curr)


look_and_say(25)

