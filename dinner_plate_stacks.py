import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = []
        self.capacity = capacity
        self.valid = []


    def push(self, val: int) -> None:
        # O(logN) time.
        while (self.valid
               and self.valid[0] < len(self.stacks)
               and len(self.stacks[self.valid[0]]) == self.capacity):
            heapq.heappop(self.valid)

        if not self.valid:
            heapq.heappush(self.valid, len(self.stacks))

        if self.valid[0] == len(self.stacks):
            self.stacks.append([])

        self.stacks[self.valid[0]].append(val)


    def pop(self) -> int:
        # O(logN) time.
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return self.popAtStack(len(self.stacks) - 1)


    def popAtStack(self, index: int) -> int:
        # O(logN) time.
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.valid, index)
            return self.stacks[index].pop()

        return -1

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
