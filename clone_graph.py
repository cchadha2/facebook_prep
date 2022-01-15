"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        cloned_nodes = [None] * 100

        # O(E + V) time for DFS and O(V) space for call stack and
        # cloned_nodes list.
        def populate_neighbours(curr):
            idx = curr.val - 1
            if cloned_nodes[idx]:
                return

            if not cloned_nodes[idx]:
                cloned_nodes[idx] = Node(curr.val)
                for neighbour in curr.neighbors:
                    if not cloned_nodes[neighbour.val - 1]:
                        populate_neighbours(neighbour)
                    cloned_nodes[idx].neighbors.append(
                        cloned_nodes[neighbour.val - 1])

        populate_neighbours(node)
        return cloned_nodes[0]
