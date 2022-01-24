from math import inf

# O(N) time and space solution.
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.idxs = {}
        
        for idx, word in enumerate(wordsDict):
            self.idxs.setdefault(word, []).append(idx)
            

    def shortest(self, word1: str, word2: str) -> int:
        p1 = p2 = 0
        
        dist = inf
        while p1 < len(self.idxs[word1]) and p2 < len(self.idxs[word2]):
            dist = min(dist, abs(self.idxs[word1][p1] - self.idxs[word2][p2]))
            
            if self.idxs[word1][p1] <= self.idxs[word2][p2]:
                p1 += 1
            else:
                p2 += 1
            
        return dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
