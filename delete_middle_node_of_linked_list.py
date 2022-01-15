# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """O(N) time and O(1) space"""

        # Find length of linked list.
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        if n == 1:
            return

        # Go to n // 2 index and delete next node.
        target = (n // 2) - 1
        curr = 0
        node = head
        while curr < target:
            node = node.next
            curr += 1

        node.next = node.next.next

        return head



    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """O(N) time and O(1) space but with only one pass"""
        if not head.next:
            return

        slow = fast = head
        prev = ListNode(next=slow)
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

        prev.next = prev.next.next

        return head
