class Solution:
    def uniqueLetterString(self, S):
        
        index = {char: [-1, -1] for char in string.ascii_uppercase}
        res = 0
        
        for idx, char in enumerate(S):
            # Track indices of last two occurrences.
            second_prev, prev = index[char]
            
            # This character is unique at all combinations of indices
            # between (last occurrence and itself) * (last occurrence - second last occurrence)
            # e.g. "XXXXAXXAXXXAXXX" where we can find the number of places the second "A"
            # is unique using this method.
            res += (idx - prev) * (prev - second_prev)
            index[char] = [prev, idx]
            
        for second_prev, prev in index.values():
            # Then we find the number of places the last occurrence
            # is unique as this wouldn't have been caught be previous loop.
            res += (len(S) - prev) * (prev - second_prev)
            
        return res
        
