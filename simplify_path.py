"""
example = "/a/./b//../../c/"
output = "/c"

Approach:
    - Split on "/" ("", "a", ".", "b", "/", "..", "..", "c", "")
    - Iterate over the chars from left to right
    - Use a stack to add the alphanum levels. If we get a ".", do nothing, and if we get a ".." and there is a value on the stack, pop it
    - Join the contents of the stack with a "/" separator and add a "/" to the start

O(N) time for split, iteration, and final join. O(N) space for the stack and the new string created for the resulting canonical path.

Could improve space used for split by using a regex instead.
"""
import re


def canonical_path(path):

    stack = []

    for level in path.split("/"):
        if not level or level == "/" or level == ".":
            continue

        if level == "..":
            if stack:
                stack.pop()
        else:
            stack.append(level)

    return "/" + "/".join(stack)


def canonical_path(path):

    stack = []
    for match in re.finditer(r"(?<=/)([\w\.]+)/?", path):
        level = match.group(1)
        if not level or level == ".":
            continue

        if level == "..":
            if stack:
                stack.pop()
        else:
            stack.append(level)

    return "/" + "/".join(stack)
