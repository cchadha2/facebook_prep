class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        """O(N) time and space solution."""
        duplicates = {}
        node = head
        while node:
            if node.val in duplicates:
                duplicates[node.val] = True
            else:
                duplicates[node.val] = False

            node = node.next

        dummy = prev = ListNode(next=head)
        curr = head
        while curr:
            if duplicates[curr.val]:
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next

        return dummy.next

    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        """O(N^2) time and O(1) space solution."""

        def remove_duplicates(temp_head, node):
            val = node.val
            prev = temp_head.next
            curr = node.next
            duplicate = False
            while curr:
                if curr.val == val:
                    prev.next = curr.next
                    duplicate = True
                else:
                    prev = prev.next

                curr = curr.next

            if duplicate:
                temp_head.next = temp_head.next.next

            return duplicate

        dummy = prev = ListNode(next=head)
        curr = head
        while curr:
            if not remove_duplicates(prev, curr):
                prev = prev.next

            curr = curr.next

        return dummy.next
