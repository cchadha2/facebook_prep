class Solution:
    def countArrangement(self, n: int) -> int:
        
        arr = list(range(1, n + 1))
        output = 0
        
        # O(N^2) time as we iterate over all N, N - 1, N - 2, etc. elems
        # at each of N calls.
        # Also O(N) space due to arr list and call stack.
        def create_perm(curr_idx):
            if curr_idx > n:
                nonlocal output
                output += 1
                return
            
            for idx in range(curr_idx - 1, n):
                num = arr[idx]
                if not num % curr_idx or not curr_idx % num:
                    arr[curr_idx - 1], arr[idx] = arr[idx], arr[curr_idx - 1]
                    
                    create_perm(curr_idx + 1)
                    
                    arr[curr_idx - 1], arr[idx] = arr[idx], arr[curr_idx - 1]
                    
        create_perm(1)
        return output
                
                
