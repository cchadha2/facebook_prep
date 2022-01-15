# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """O(N) time and O(1) space."""

        # Determine if the list has a cycle.
        def has_cycle(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                if slow is fast:
                    return slow

        slow = has_cycle(head)
        if not slow:
            return

        node = head
        while not slow is node:
            node = node.next
            slow = slow.next

        return node
