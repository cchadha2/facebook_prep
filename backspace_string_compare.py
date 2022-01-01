"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow-up:
    - Do this in O(1) space?
"""
from itertools import zip_longest

def backspace(s, t):
    """O(S + T) time and space"""

    def delete_chars(word):
        stack = []

        for char in s:
            if char.islower():
                stack.append(char)
            elif stack:
                stack.pop()

        return stack

    return delete_chars(s) == delete_chars(t)


def backspace(s, t):
    """O(S + T) time and O(1) space"""

    def gen_chars(word):
        idx = len(word) - 1
        skip = 0

        while idx >= 0:

            if not word[idx].islower():
                skip += 1
            elif not skip:
                yield word[idx]
            else:
                skip -= 1

            idx -= 1

    for s_char, t_char in zip_longest(gen_chars(s), gen_chars(t)):
        if s_char is None and t_char:
            return False
        elif t_char is None and s_char:
            return False
        elif t_char != s_char:
            return False


    return True
