class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root):
        # O(N) time and space for building nodes list.
        self.nodes = [None]
        self.nodes.extend(self._inorder(root))
        self.pointer = 0

    # O(1) time and space.
    def next(self):
        if not self.hasNext():
            raise StopIteration("No next number in tree")

        self.pointer += 1
        return self.nodes[self.pointer]

    # O(1) time and space.
    def hasNext(self):
        return not self.pointer == len(self.nodes) - 1

    # O(N) time where N is number of nodes and between O(logN) and O(N) space for call stack.
    def _inorder(self, node):
        if not node:
            return

        yield from self._inorder(node.left)

        yield node.val

        yield from self._inorder(node.right)


# Optimised for O(1) (amortized) time and O(h) space for next and hasNext()
# without creating sorted list of nodes at initialization.
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self._inorder(root)

    # O(1) time and O(h) space.
    def next(self):
        if not self.stack:
            raise StopIteration("No more nodes in tree")

        node = self.stack.pop()

        self._inorder(node.right)

        return node.val

    # O(1) time and O(h) space.
    def hasNext(self):
        return bool(self.stack)

    def _inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

        
