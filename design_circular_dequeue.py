class Node:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head = self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if not self.head:
            self.head = self.tail = Node(value)
        else:
            node = Node(value, next=self.head)
            self.head.prev = node
            self.head = node

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if not self.tail:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value, prev=self.tail)
            self.tail = self.tail.next

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.val if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.tail.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return not self.size

    def isFull(self) -> bool:
        return self.size == self.k



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
