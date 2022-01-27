class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """O(N) time and O(N) space for reverse index hashmap"""
        reverse_idx = {}
        for idx, word in enumerate(wordsDict):
            reverse_idx.setdefault(word, []).append(idx)
            
        p1 = p2 = 0
        dist = len(wordsDict)
        while p1 < len(reverse_idx[word1]) and p2 < len(reverse_idx[word2]):
            dist = min(dist, abs(reverse_idx[word1][p1] - reverse_idx[word2][p2]))
            
            if reverse_idx[word1][p1] < reverse_idx[word2][p2]:
                p1 += 1
            else:
                p2 += 1
                
        return dist
    
    
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """O(N*M) time where N is number of words and M is length of longer word. O(1) space."""
        p1 = p2 = -1
        dist = len(wordsDict)
        
        for idx, word in enumerate(wordsDict):
            
            if word == word1:
                p1 = idx
            elif word == word2:
                p2 = idx
                
                
            if p1 > -1 and p2 > -1:
                dist = min(dist, abs(p1 - p2))
        
        return dist
