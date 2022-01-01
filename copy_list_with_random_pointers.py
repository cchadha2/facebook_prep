"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example:
3 -> 4 -> 1 -> 2 -> 3
4 -> 2, 3 -> 1, 1 -> null, 2 -> 4, 3 -> 3

Approach:
    1. Add an order attribute to the original nodes to keep track of their index.
    2. Create an array of nodes (O(N) space).
    3. Create node copies as we iterate through our original list. While doing so, add the new node to our array under the index of the original node.
       Also set the random attribute of the new node to the index of the original random node so we can later look it up in the array.
    4. Iterate through our copied list and set the random pointer to the node itself in the array by looking up its index from 3.

O(N) time and O(N) space for random pointers array.
"""
class Node:

    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def deep_copy(head):
    if not head:
        return
    # Add order attribute to original nodes to differentiate between them.
    # O(N) time and O(1) space.
    node = head
    order = 1
    while node:
        node.order = order
        node = node.next
        order += 1

    # Initialise index of order to node.
    # O(N) time and space.
    random_nodes = [None] * order

    # Create our node copies, setting the random attribute to the index of the node.
    # O(N) time and O(1) space.
    dummy = new_head = Node(0)
    node = head
    while node:
        new_head.next = Node(node.val)
        # Add the current node to the random_nodes list.
        random_nodes[node.order] = new_head.next
        # Some nodes can point to None in their random attribute.
        if node.random:
            new_head.next.random = node.random.order
        node = node.next
        new_head = new_head.next

    # Go back through our copied list and lookup the appropriate random nodes.
    # O(N) time and O(1) space.
    new_head = dummy.next
    while new_head:
        if new_head.random:
            new_head.random = random_nodes[new_head.random]

        new_head = new_head.next

    return dummy.next

# Without redundant iteration at the end to set indices to pointers.
def deep_copy(head):
    if not head:
        return

    # Add idx attribute to original nodes to differentiate between them.
    # O(N) time and O(1) space.
    node = head
    idx = 0
    while node:
        node.idx = idx
        node = node.next
        idx += 1

    # Initialise index of order to node.
    # O(N) time and space.
    random_nodes = [None] * idx

    # Create our node copies, setting the random attribute to the index of the node.
    # O(N) time and O(1) space.
    dummy = new_head = Node(0)
    node = head
    while node:
        # Add the current node to the random_nodes list.
        if not random_nodes[node.idx]:
            random_nodes[node.idx] = Node(node.val)

        new_head.next = random_nodes[node.idx]

        # Some nodes can point to None in their random attribute.
        if node.random:
            if not random_nodes[node.random.idx]:
                random_nodes[node.random.idx] = Node(node.random.val)

            new_head.next.random = random_nodes[node.random.idx]

        node = node.next
        new_head = new_head.next

    return dummy.next

# O(N) time and O(1) space solution.
def deep_copy(head):
    if not head:
        return

    # Create new nodes next to original nodes.
    # O(N) time and O(1) space (not counting new nodes created as extra space).
    node = head
    while node:
        node.next = Node(node.val, node.next)
        node = node.next.next

    # Set random pointers for the copied nodes.
    # O(N) time and O(1) space.
    node = head
    while node:
        if node.random:
            node.next.random = node.random.next

        node = node.next.next

    # Unlink the original nodes from the copied nodes.
    # O(N) time and O(1) space.
    node = head
    new_head = copied_node = head.next
    while node.next.next:
        node = node.next.next
        copied_node.next = node.next
        copied_node = copied_node.next

    return new_head
