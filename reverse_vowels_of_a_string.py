"""
Approach:
    - Iterate through the string and find the indices of the vowels (O(N) time and O(1) space)
    - Save the character and the index as tuples and add them to an array (O(N) space)
    - Create a new array of the chars of s (as a string is immutable)
    - Use two pointers from either end of the tuple array to swap the left and right chars
    - Move both pointers inwards after the swap
    - Join the chars array into a new string (O(N) time and space)


example = "leetcode"
vowels = [("e", 1), ("e", 2), ("o", 5), ("e", 7)]
chars = ["l", "e", "e", "t", "c", "o", "d", "e"]
p1 = 0
p2 = len(vowels) - 1

On first iteration:
chars = ["l", "e", "e", "t", "c", "o", "d", "e"]
p1 = 1
p2 = 2

On second iteration:
chars = ["l", "e", "o", "t", "c", "e", "d", "e"]


Overall O(N) time and space.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:

        possible_vowels = set(("A", "E", "I", "O", "U", "a", "e", "i", "o", "u"))
        chars = list(s)
        vowels = list(filter(lambda idx: chars[idx] in possible_vowels, range(len(chars))))

        p1, p2 = 0, len(vowels) - 1
        while p1 < p2:
            left_idx, right_idx = vowels[p1], vowels[p2]

            chars[left_idx], chars[right_idx] = chars[right_idx], chars[left_idx]

            p1 += 1
            p2 -= 1

        return "".join(chars)

        
