from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Iterate over rooms, looking for each gate.
        # Add the gate to a stack when we find it.
        stack = []
        m, n = len(rooms), len(rooms[0])
        
        # O(MN) time and O(1) space.
        for row in range(m):
            for col in range(n):
                if not rooms[row][col]:
                    stack.append((row, col))
        
        
        # Carry out a breadth-first search from each gate,
        # setting the minimum distance to each room as we go.
        # Only proceed in the BFS if the distance to the current
        # room is less than the one currently in the rooms array.
        # O(MN) time and O(MN) space.
        queue = deque()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for gate_row, gate_col in stack:
            
            queue.append((0, gate_row, gate_col))
            while queue:
                distance, row, col = queue.popleft()
                
                if rooms[row][col] and distance >= rooms[row][col]:
                    continue
                
                rooms[row][col] = distance
                
                for row_inc, col_inc in directions:
                    next_row, next_col = row + row_inc, col + col_inc
                    
                    if (0 <= next_row < m
                        and 0 <= next_col < n
                        # Next room is not a gate.
                        and rooms[next_row][next_col]):
                        queue.append((distance + 1, next_row, next_col))
                        
        return rooms
