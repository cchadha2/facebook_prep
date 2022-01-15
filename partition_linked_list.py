# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """O(N) time and O(1) space."""

        # Set tail pointer and count length of list.
        node = head
        length = 0
        while node:
            if not node.next:
                tail = node

            length += 1
            node = node.next

        if length == 1:
            return head

        # Go over list again and remove any nodes >= partition.
        # Put those nodes at the end of the list.
        node = head
        dummy = prev = ListNode(next=node)
        for _ in range(length):
            if node.val >= x and not node is tail:
                temp = node
                prev.next = node.next
                node = node.next

                tail.next = temp
                tail = tail.next
                tail.next = None
            else:
                prev = prev.next
                node = node.next


        return dummy.next
