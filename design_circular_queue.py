class Node:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head = self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if not self.head:
            self.head = self.tail = Node(value)
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            node = Node(value, prev=self.tail, next=self.head)
            self.head.prev = node
            self.tail.next = node
            self.tail = self.tail.next

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.size == 1:
            self.head = self.tail = None
        else:
            node = self.head

            self.head = self.head.next

            node.prev.next = node.next
            node.next.prev = node.prev

        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return not self.size

    def isFull(self) -> bool:
        return self.size == self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
