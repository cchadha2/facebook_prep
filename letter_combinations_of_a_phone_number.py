"""
Because there are a variable number of characters between numbers - 3 chars for
all numbers but 7 and 9 which have 4 chars each, we cannot simply have 3 for
loops, iterating over the chars of each digit and creating new combinations.

Instead, we can use recursive functions which return the chars of the respective
digit in order and we can create a new string by joining the characters given
by each recursive function.


This will run in O(N) time where N is length of the digits string and O(N) space
for the call stack in the same way.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7":"pqrs", "8": "tuv", "9": "wxyz"}


        def generate_chars(idx):
            if idx >= len(digits):
                return []

            output = []
            suffixes = generate_chars(idx + 1)
            if not suffixes:
                return list(mapping[digits[idx]])

            for char in mapping[digits[idx]]:
                for suffix in suffixes:
                    output.append(char + suffix)

            return output

        return generate_chars(0)
