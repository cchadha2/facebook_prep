class Solution:
    def isValid(self, s: str) -> bool:
        # O(N) time and space solution.
         
        stack = []
        matching = {"}": "{", ")": "(", "]": "["}
        
        for char in s:
            if char in matching:
                if (not stack
                    or matching[char] != stack.pop()):
                    return False
            else:
                stack.append(char)
                
        return not stack
