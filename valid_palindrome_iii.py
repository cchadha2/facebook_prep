from functools import cache

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        @cache
        def max_palindrome(start, end):
            if start > end:
                return 0
            elif start == end:
                return 1

            if s[start] == s[end]:
                return 2 + max_palindrome(start + 1, end - 1)
            else:
                return max(max_palindrome(start + 1, end),
                           max_palindrome(start, end - 1))

        return max_palindrome(0, len(s) - 1) >= (len(s) - k)


    def isValidPalindrome(self, s: str, k: int) -> bool:

        memo = [[None] * len(s) for _ in range(len(s))]

        for row in range(len(s)):
            memo[row][row] = 1

        step = 1
        while step < len(s):
            for row in range(len(s) - step):
                col = row + step
                if step == 1:
                    if s[row] == s[col]:
                        memo[row][col] = 2
                    else:
                        memo[row][col] = 1
                else:
                    if s[row] == s[col]:
                        memo[row][col] = 2 + memo[row + 1][col - 1]
                    else:
                        memo[row][col] = max(memo[row + 1][col],
                                             memo[row][col - 1])

            step += 1

        return memo[0][-1] >= (len(s) - k)


        
