class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
         
        n = 8
        board = [[set() for _ in range(n)] for _ in range(n)]
        for i, (row, col) in enumerate(positions):
            positions[i][0] = row - 1
            positions[i][1] = col - 1
            
        
        rook_directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        bishop_directions = ((1, 1), (-1, -1), (1, -1), (-1, 1))
        directions = {"rook": rook_directions,
                      "bishop": bishop_directions,
                      "queen": rook_directions + bishop_directions}
        
        all_time = set(range(1, n)) # move for at most 8 seconds because onlnext_col 8next_row8 board
        
        
        def recur(i):
            if i == len(pieces):
                # if the last piece has a valid destination, count this move combination
                return 1
            
            ans = 0
            row, col = positions[i]
            if not board[row][col] & all_time:
                # if the position of piece i is available all the time,
                # consider not moving this piece at all.
                board[row][col] |= all_time
                
                ans += recur(i + 1)
                
                board[row][col].clear() # undo the move for the current piece
       
            for row_inc, col_inc in directions[pieces[i]]:
                # consider a direction the current piece moves to
                next_row, next_col = row + row_inc, col + col_inc
                count = 1 #(https://leetcode.com/problems/valid-parentheses) time counter
                while (0 <= next_row < n
                       and 0 <= next_col < n
                       and count not in board[next_row][next_col]):
                    
                    # if board[next_row][next_col] is available at time count, the move is valid
                    board[next_row][next_col].add(count) 
                    count += 1
                    
                    rest = set(range(count, n))
                    if not board[next_row][next_col] & rest:
                        # if the board is available for the rest of the time, the move might stop here
                        board[next_row][next_col] |= rest
                        
                        ans += recur(i + 1)
                        
                        board[next_row][next_col] -= rest
                        
                    next_row += row_inc
                    next_col += col_inc
                    
                # undo the last update
                count -= 1
                next_row -= row_inc
                next_col -= col_inc
                while count:
                    # undo the updates of the piece
                    board[next_row][next_col].remove(count)
                    count -= 1
                    next_row -= row_inc
                    next_col -= col_inc
            return ans
        
        return recur(0)
