# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        O(N) time and O(1) space.
        """

        # Copy values of next node into current node.
        # When we reach second to last node, set the next pointer to None.
        curr = node
        second_to_last = None
        while curr and curr.next:
            curr.val = curr.next.val

            if not curr.next.next:
                second_to_last = curr

            curr = curr.next


        second_to_last.next = None
