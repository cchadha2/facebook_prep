class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        ans = curr = prev = 0
        for idx, char in enumerate(s):
            if not idx or char != s[idx - 1]:
                ans += min(prev, curr)
                prev = curr
                curr = 1 
            else:
                curr += 1
             
        return ans + min(prev, curr)
       
