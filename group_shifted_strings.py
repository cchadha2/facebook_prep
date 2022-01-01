"""
Note that we're looking for the distance between two chars, knowing that the
second char has been shifted up x time. This is trivial between two characters
such as "z" and "a" as we simply subtract ord("z") - ord("a").

The tricky case is when the characters wrap around and we have something like
"b" shifted to "a". ord("a") - ord("b") will be -1 but the actual distance
between these two chars is 25 as we shifted up from "b" to "a" and not down.
i.e. "b" -> "c" -> "d" -> ... -> "z" -> "a" which represents 25 shifts up.

To get the correct number with the wraparound, we simply do:

distance = ord(char2) - ord(char1) % 26

as there are 26 characters in our range.

This works because we A // B * B + A % B == A (as per the C99 standard).
For example, if A == -1 and B == 26:

1. -1 // 26 = -1 as -1 / 26 = -0.03 and floor(-0.03) = -1
2. -1 // 26 * 26 = (-1) * 26 = -26
3. -1 // 26 * 26 + -1 % 26 == -1
   -26 + (-1 % 26) == -1
   -1 % 26 == 25

To group strings, maintain a hashmap with keys as distances between adjacent
characters so that "az" and "ba" both map to (25, ). The groups are then simply
the values of the hashmap (which should be lists of strings).
"""
def group_shifted_strings(strings):

    num_chars = 26
    groupings = {}

    def calculate_distances(string):
        for idx in range(len(string)):
            yield ord(string[idx]) - ord(string[idx - 1]) % num_chars

    for string in strings:
        # e.g. "az" -> (25, ) and "xyz" -> (1, 1)
        groupings.setdefault(tuple(calculate_distances(string)), []).append(string)

    return list(groupings.values())
