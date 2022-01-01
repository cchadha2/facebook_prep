from collections import OrderedDict

class LRUCache:
    """O(1) time for get and put and O(N) space for ordered dict."""

    # O(N) space for ordered dict.
    def __init__(self, capacity):
        self.table = OrderedDict()
        self.capacity = capacity

    # O(1) time worst case.
    def get(self, key):
        if not key in self.table:
            return -1

        value = self.table[key]
        self.table.move_to_end(key)
        return value


    # O(1) time worst case.
    def put(self, key, value):
        if key in self.table:
            self.table[key] = value
            self.table.move_to_end(key)
            return

        self.table[key] = value
        if len(self.table) > self.capacity:
            self.table.popitem(last=False)

# Without OrderedDict.
class Node:

    def __init__(self, key, val, prev_node=None, next_node=None):
        self.key = key
        self.val = val
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        return f"Node(key={self.key}, val={self.val})"


class LRUCache:
    """O(1) time for get and put and O(N) space for nodes of doubly linked list."""

    def __init__(self, capacity: int):
        # Keep a hashmap of key to the node in the ll for quick access.
        self.table = {}
        self.head = self.tail = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.table:
            return -1

        self._move_to_end(key)
        return self.table[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.table[key].val = value
            self.table[key].key = key
            self._move_to_end(key)
            return

        self._append(key, value)
        if len(self.table) > self.capacity:
            self._pop()

    def _move_to_end(self, key):
        if self.tail is self.table[key]:
            return

        node = self.table[key]
        # Remove node from linked list
        # Place at end of list
        if node.prev_node:
            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node
        else:
            self.head = self.head.next_node
            self.head.prev_node = None

        node.next_node = None
        node.prev_node = self.tail
        self.tail.next_node = node
        self.tail = node

    def _append(self, key, value):
        node = Node(key, value, prev_node=self.tail)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next_node = node

        self.tail = node
        self.table[key] = node

    def _pop(self):
        node = self.head
        if node is self.tail:
            self.tail = self.head = None
            return

        self.head = node.next_node
        node.next_node = self.head.prev_node = None
        del self.table[node.key]
