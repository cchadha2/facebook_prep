from math import inf

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        
        n = len(grid)
        
        def check_possible(time):
            if time < grid[0][0]:
                return False
            
            visited = set()
            
            stack = [(0, 0)]
            minimum_time = inf
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            
            while stack:
            
                row, col = stack.pop()
                
                visited.add((row, col))
               
                if row == n - 1 and col == n - 1:
                    return True
                
                for row_inc, col_inc in directions:
                    next_row, next_col = row + row_inc, col + col_inc
                    
                    if (not 0 <= next_row < n
                        or not 0 <= next_col < n
                        or (next_row, next_col) in visited
                        or grid[next_row][next_col] > time):
                        continue
                        
                    stack.append((next_row, next_col))
        
            return False
        
        lo, hi = 0, n**2
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if check_possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1
                
        return lo
