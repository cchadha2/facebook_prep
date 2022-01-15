# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """O(N) time and O(1) space."""

        nth_node = runner = head
        dummy = prev = ListNode(next=head)
        k = 0
        while runner and k < n:
            runner = runner.next
            k += 1

        while runner:
            prev = prev.next
            nth_node = nth_node.next
            runner = runner.next

        prev.next = nth_node.next

        return dummy.next
