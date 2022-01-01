"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Constraints:
    - We must include all characters of s in the output
    - There is no guarantee of a word existing in s
    - This means we can get an empty string as input

Approach:
    - Need to quickly look up if word is in wordDict -> cast to a hash set for O(1) lookup. This is O(W) time and space where W is number of words in wordDict.
    - Create an empty output list to append results to
    - Use a list to add words to if they are in the wordDict
    - Track start and end indices in our function and use them to check if a substring is in the wordDict (O(substring) time and space for string creation).
    - When the start exceeds the length of s, we have a valid arrangement of words so add the string of the list to the output list and pop the last item
    - If the end exceeds the length of s, simply return

Could cache results between certain indices to improve time complexity.

Worst-case:
s = "abcd"
wordDict = ["a", "ab", "abc", "abcd", "b", "bc", "bcd", "c", "cd", "d"]

len(wordDict) => 10
len(s) => 4

                    break_words(start=0, words=[])
                  /          |              |      \
                "a"         "ab"          "abc"    "abcd"
              /  |  \       /  \            |
           "b" "bc" "bcd" "c"  "cd"        "d"
          /  \   \        /
        "c" "cd" "d"    "d"
        /
      "d"

Total number of calls after initial call = 15 calls => O(2^N) time where N is number of characters in s.
For each leaf, we do an O(N) operation to create the output string or to create the string to add to words.

Therefore, we have an O(N*2^N) time and O(W + N) space solution.
"""


def word_break(s, wordDict):

    # O(W) time and space.
    wordDict = set(wordDict)
    output = []

    def break_words(start, words):
        if start >= len(s):
            # O(N) time and space.
            output.append(" ".join(words))
            return

        for sub_idx in range(start + 1, len(s) + 1):
            word = s[start : sub_idx]
            if word in wordDict:
                words.append(word)
                break_words(sub_idx, words)
                words.pop()


    break_words(0, [])
    return output
