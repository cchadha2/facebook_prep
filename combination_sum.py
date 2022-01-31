class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # O(ClogC) time and O(C) space.
        candidates.sort()
        output = []
        path = []
        
        
        # O(C^(T/M)) time and O(T/M) space for path.
        # Where T is target and M is the smallest value in candidates.
        def combo_sum(idx, curr):
            if curr == target:
                output.append(path.copy())
                return
            
            for next_idx in range(idx, len(candidates)):
                if curr + candidates[next_idx] > target:
                    break
                    
                path.append(candidates[next_idx])
                
                combo_sum(next_idx, curr + candidates[next_idx])
                
                path.pop()
                
        combo_sum(0, 0)
        return output
                
