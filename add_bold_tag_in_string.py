from itertools import islice

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        locations = []
        
        # Find all potentially overlapping start and end indices
        # of each word in words.
        # O(S^2W^2) time.
        for word in words:
            # O(SW) time (from source code).
            start = s.find(word)
            # O(S^2W) time.
            while start != -1:
                locations.append([start, start + len(word)])
                # O(SW) time.
                start = s.find(word, start + 1)
                
        if not locations:
            return s
        
        # Merge intervals.
        locations.sort()
        start, end = locations[0][0], locations[0][1]
        res = s[:start]
        for next_start, next_end in islice(locations, 1, None):
            # Overlap.
            if next_start <= end:
                end = max(end, next_end)
            else:
                res += "<b>" + s[start : end] + "</b>"
                res += s[end : next_start]
                start, end = next_start, next_end
            
        res += "<b>" + s[start : end] + "</b>" + s[end:]
        return res
