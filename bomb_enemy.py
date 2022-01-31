class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """O(MN) time and O(MN) space."""
        
        m, n = len(grid), len(grid[0])
        # O(MN) time and space.
        rows = [row.copy() for row in grid]
        cols = [row.copy() for row in grid]
        maximum = 0
        
        # O(MN) time and O(1) space.
        # This is because we don't repeat calculations
        # for rows and columns unless there is a wall.
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "0":
                    count = 0
                    
                    col_count = 0
                    if cols[row][col] == "0":
                        # O(M) time.
                        for curr_row in range(row, m):
                            if grid[curr_row][col] == "E":
                                col_count += 1
                            elif grid[curr_row][col] == "W":
                                break
                        for curr_row in range(row, -1, -1):
                            if grid[curr_row][col] == "E":
                                col_count += 1
                            elif grid[curr_row][col] == "W":
                                break
                        for curr_row in range(row, m):
                            if grid[curr_row][col] == "0":
                                cols[curr_row][col] = col_count
                            elif grid[curr_row][col] == "W":
                                break
                        for curr_row in range(row, -1, -1):
                            if grid[curr_row][col] == "0":
                                cols[curr_row][col] = col_count
                            elif grid[curr_row][col] == "W":
                                break
                                
                    count += cols[row][col]
                            
                    row_count = 0  
                    if rows[row][col] == "0":
                        # O(N) time.
                        for curr_col in range(col, n):
                            if grid[row][curr_col] == "E":
                                row_count += 1
                            elif grid[row][curr_col] == "W":
                                break
                        for curr_col in range(col, -1, -1):
                            if grid[row][curr_col] == "E":
                                row_count += 1
                            elif grid[row][curr_col] == "W":
                                break
                        for curr_col in range(col, n):
                            if grid[row][curr_col] == "0":
                                rows[row][curr_col] = row_count
                            elif grid[row][curr_col] == "W":
                                break
                        for curr_col in range(col, -1, -1):
                            if grid[row][curr_col] == "0":
                                rows[row][curr_col] = row_count
                            elif grid[row][curr_col] == "W":
                                break
                                
                    count += rows[row][col]
                        
                    maximum = max(maximum, count)
                    
        
        return maximum
                    
