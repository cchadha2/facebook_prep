from functools import cache

class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        
        # Function to get the ending index of the numeric
        # substring, starting at `start`.
        def get_valid_prefix_length(numeric_sub, start):
            end = start
            while end < len(numeric_sub) and numeric_sub[end].isdigit():
                end += 1
                
            return end
        
        
        # Get all possible lengths that numeric substring could
        # represent
        @cache
        def possible_lengths(numeric_sub):
            lengths = {int(numeric_sub)}
            
            for split_idx in range(1, len(numeric_sub)):
                for prefix_length in possible_lengths(numeric_sub[:split_idx]):
                    for suffix_length in possible_lengths(numeric_sub[split_idx:]):
                        lengths.add(prefix_length + suffix_length)
                    
            return lengths
        
        
        @cache
        def compare_substrings(p1, p2, diff):
            """Compare substrings s1[p1:] and s2[p2:]."""
            
            # If both have reached end and there is no difference
            # found between them.
            if p1 == len(s1) and p2 == len(s2):
                return not diff
            
            # p1 hasn't reached the end and s1[p1] is a digit.
            if p1 < len(s1) and s1[p1].isdigit():
                next_p1 = get_valid_prefix_length(s1, p1)
                
                for length in possible_lengths(s1[p1 : next_p1]):
                    # s2's lead is decreased by length (can be negative).
                    if compare_substrings(next_p1, p2, diff - length):
                        return True
                    
            # p2 hasn't reached the end and s2[p2] is a digit.
            elif p2 < len(s2) and s2[p2].isdigit():
                next_p2 = get_valid_prefix_length(s2, p2)
                
                for length in possible_lengths(s2[p2 : next_p2]):
                    # s2's lead is increased by length.
                    if compare_substrings(p1, next_p2, diff + length):
                        return True
                    
            # If both indices are on par.
            elif not diff:
                # if only one of them as reached the end or current chars
                # are not the same.
                if p1 == len(s1) or p2 == len(s2) or s1[p1] != s2[p2]:
                    return False
                
                return compare_substrings(p1 + 1, p2 + 1, 0)
            
            elif diff > 0:
                if p1 == len(s1):
                    return False
                
                return compare_substrings(p1 + 1, p2, diff - 1)
            
            else:
                if p2 == len(s2):
                    return False
                
                return compare_substrings(p1, p2 + 1, diff + 1)
            
            
        return compare_substrings(0, 0, 0)
