from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """O(ST) time and O(T) space."""
        if len(t) > len(s):
            return ""
        
        # O(1) time and space.
        s_counts = [0] * 128
        t_counts = [0] * 128
        # O(T) time and space.
        t_chars = set(t)
        
        # O(T) time and O(1) space.
        def compare_counts():
            for char in t_chars:
                if s_counts[ord(char)] < t_counts[ord(char)]:
                    return False
                
            return True
            
        # O(T) time.
        end = 0
        while end < len(t):
            s_counts[ord(s[end])] += 1
            t_counts[ord(t[end])] += 1
            end += 1
            
        # O(T) time and space.
        if compare_counts():
            return s[:end]
        
        # O(ST) time and O(1) space at worst.
        lo, hi = 0, len(s)
        start = 0
        contains = False
        while start < end and end < len(s):
            
            while end < len(s) and not compare_counts():
                s_counts[ord(s[end])] += 1
                end += 1
                
            while start < end and compare_counts():
                if (end - start) <= (hi - lo):
                    lo, hi = start, end
                    contains = True
             
                s_counts[ord(s[start])] -= 1
                start += 1
                
                
        # O(S) time and space at worst.
        return s[lo : hi] if contains else ""
                
                
        
            
        
