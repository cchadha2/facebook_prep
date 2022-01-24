class MaxStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, max(x, self.stack[-1][1])))
        

    def pop(self) -> int:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def peekMax(self) -> int:
        return self.stack[-1][1]
        

    def popMax(self) -> int:
        temp = []
        while self.stack and self.stack[-1][0] != self.stack[-1][1]:
            temp.append(self.stack.pop()[0])
            
        res = self.stack.pop()[0]
        
        while temp:
            self.push(temp.pop())
        
        return res
        
