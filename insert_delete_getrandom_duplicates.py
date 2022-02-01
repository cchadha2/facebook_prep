import random

class RandomizedCollection:
    """O(1) average time for each operation (not counting array resizing).
       O(N) space for hashtable and stack
       
    """

    def __init__(self):
        self.stack = []
        self.table = {}
        

    def insert(self, val: int) -> bool:
        self.stack.append(val)
        
        res = val in self.table
        if not res:
            self.table[val] = set()
            
        self.table[val].add(len(self.stack) - 1)
        return not res
            
    def remove(self, val: int) -> bool:
        if not self.stack or not val in self.table:
            return False
        
        last_elem = self.stack[-1]
        last_elem_idx = len(self.stack) - 1
        self.table[last_elem].remove(last_elem_idx)
        
        if not last_elem == val:
            val_idx = self.table[val].pop()
            self.table[last_elem].add(val_idx)
            self.stack[last_elem_idx], self.stack[val_idx] = self.stack[val_idx], self.stack[last_elem_idx]
        
        if not self.table[val]:
            del self.table[val]
            
        self.stack.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.stack)
        
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
