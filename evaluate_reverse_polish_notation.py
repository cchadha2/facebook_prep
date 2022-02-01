class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """O(N) time and space where N is number of tokens."""
        
        stack = []
        
        for token in tokens:
            if token.isnumeric() or (token.startswith("-") and len(token) > 1):
                stack.append(int(token))
            else:
                curr, prev = stack.pop(), stack.pop()
                
                if token == "+":
                    stack.append(prev + curr)
                elif token == "-":
                    stack.append(prev - curr)
                elif token == "*":
                    stack.append(prev * curr)
                else:
                    if prev < 0 and curr < 0:
                        stack.append(-prev // -curr)
                    elif prev < 0:
                        prev = -prev
                        stack.append(prev // curr)
                        stack[-1] = -stack[-1]
                    elif curr < 0:
                        curr = -curr
                        stack.append(prev // curr)
                        stack[-1] = -stack[-1]
                    else:
                        stack.append(prev // curr)
                        
                        
        return stack[0]
                    
