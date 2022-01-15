class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node(val={self.val}, next={self.next})"


class MyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        #print(f"get {index=}", self.size)
        if not 0 <= index < self.size:
            return -1
        elif index == self.size - 1:
            return self.tail.val

        #print(self.head, index, self.size)
        node = self.head
        curr_idx = 0
        while curr_idx < index:
            node = node.next
            curr_idx += 1

        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        #print(f"add at head {val=}", self.size)
        if not self.head:
            self.head = self.tail = Node(val)
        else:
            node = Node(val, next=self.head)
            self.head = node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        #print(f"add at tail {val=}, {self.tail=}", self.size)
        if not self.tail:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        #print(f"adding at {index=}", self.size)
        if not 0 <= index <= self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            node = self.head
            curr_idx = 0

            while curr_idx < index - 1:
                node = node.next
                curr_idx += 1

            if not node:
                return

            node.next = Node(val, next=node.next)

            self.size += 1

        #print(self.size)

    def deleteAtIndex(self, index: int) -> None:
        #print(f"deleting at {index=}", self.head, self.size)
        if not 0 <= index < self.size:
            return
        elif index == 0:
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
        else:
            node = self.head
            curr_idx = 0

            while curr_idx < index - 1:
                node = node.next
                curr_idx += 1

            if not node:
                return

            node.next = node.next.next

            if index == self.size - 1:
                self.tail = node

        self.size -= 1
        #print(self.size)
