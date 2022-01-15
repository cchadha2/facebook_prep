# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """O(max(l1, l2)) time and O(max(l1, l2)) space for the string of the sum and new linked list."""

        ll_sum = 0

        order = 1
        node = l1
        while node:
            ll_sum += node.val * order
            order *= 10

            node = node.next

        order = 1
        node = l2
        while node:
            ll_sum += node.val * order
            order *= 10

            node = node.next

        new_list = curr = ListNode()
        for digit in reversed(str(ll_sum)):
            curr.next = ListNode(int(digit))
            curr = curr.next

        return new_list.next
