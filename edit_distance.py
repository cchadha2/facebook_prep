class Solution:
    """O(MN) time and space solution."""
    
    
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        #    ""  h  ho hor hors horse
        # ""  0  1  2  3   4     5
        # r   1  1  2  2   3     4
        # ro  2  2  1  2   3     4
        # ros 3  3  2  2   2     3
        
        
        # If letters are equal, min distance = dist[row - 1][col - 1] as dist[row][col - 1] >= dist[row - 1][col - 1]
        # and dist[row - 1][col] >= dist[row - 1][col - 1] always.
        # Else distance = min(dist[row - 1][col], dist[row][col - 1], dist[row - 1][col - 1]) + 1
        
        dist = [[None] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for row in range(len(dist)):
            dist[row][0] = row
            
        for col in range(len(dist[0])):
            dist[0][col] = col
            
        for row_idx in range(1, len(dist)):
            for col_idx in range(1, len(dist[0])):
                
                if word2[row_idx - 1] != word1[col_idx - 1]:
                    dist[row_idx][col_idx] = min(dist[row_idx - 1][col_idx],
                                                 dist[row_idx][col_idx - 1],
                                                 dist[row_idx - 1][col_idx - 1]) + 1
                else:
                    dist[row_idx][col_idx] = dist[row_idx - 1][col_idx - 1]
                    
        return dist[-1][-1]
    
