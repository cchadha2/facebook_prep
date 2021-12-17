"""
Example:

s = "azxxzy"

"""



def remove_duplicates(s):

    stack = []
    for char in s:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()

    return "".join(stack)
       
