"""
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.


Questions:
    - Can we get an empty string? No
    - All lowercase letters? Yes
    - Can abbr be empty? No
    - Is abbr also all lowercase and digits? Yes

Approach:
    - The letters in abbr and string should match exactly
    - Any digits in abbr should be turned into an int and their value is how much we should skip ahead from a letter in string to the next letter
    - Use a while loop to go through the string and the abbr simultaneously


O(min(M, N)) time where M is number of characters in abbr and N is number of characters in string. O(1) space.
"""


def valid_abbr(string, abbr):

    skip = string_idx = abbr_idx = 0
    while string_idx < len(string) and abbr_idx < len(abbr):

        if abbr[abbr_idx] == "0":
            return False

        while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
            skip = (skip * 10) + int(abbr[abbr_idx])
            abbr_idx += 1

        string_idx += skip
        skip = 0

        if string_idx == len(string) and abbr_idx == len(abbr):
            return True
        elif (string_idx >= len(string)
              or abbr_idx >= len(abbr)
              or string[string_idx] != abbr[abbr_idx]):
            return False

        string_idx += 1
        abbr_idx += 1

    return string_idx == len(string) and abbr_idx == len(abbr)
