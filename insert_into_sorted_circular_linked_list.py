"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        elif head.next is head:
            node = Node(insertVal, next=head)
            head.next = node
            return head 
        
        node = tail = true_head = head
        inserted = False
        while True:
            if node.val <= insertVal <= node.next.val:
                node.next = Node(insertVal, next=node.next)
                inserted = True
                break
                
            node = node.next
            if node is head:
                break
                
            tail = max(node, tail, key=lambda elem: elem.val)
            if node.val < true_head.val:
                true_head = node
                
        if not inserted:
            tail.next = Node(insertVal, next=true_head)
                
        return head
                
