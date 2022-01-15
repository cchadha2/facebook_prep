class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap:

    # Reasonably long to avoid long chains.
    size = 2056

    def __init__(self):
        self.table = [[] for _ in range(self.size)]


    # O(N/M) average case time for search where N is number of elements in the
    # table and M is the size of the table (2056 in this case). O(N) worst
    # case where all of the elements hash to one index but this shouldn't be
    # the case if we have a uniform hashing function.
    # In this case, the keys are ints. If they weren't, we'd call hash(key)
    # before the modulo operation to get an integer representation of the key.
    def put(self, key: int, value: int) -> None:
        idx = key % self.size

        for node in self.table[idx]:
            if node.key == key:
                node.val = value
                return

        self.table[idx].append(Node(key, value))

    def get(self, key: int) -> int:
        idx = key % self.size

        for node in self.table[idx]:
            if node.key == key:
                return node.val

        return -1


    def remove(self, key: int) -> None:
        idx = key % self.size

        for node_idx, node in enumerate(self.table[idx]):
            if node.key == key:
                for next_idx in range(node_idx, len(self.table[idx]) - 1):
                    self.table[idx][next_idx] = self.table[idx][next_idx + 1]

                self.table[idx].pop()
                return
