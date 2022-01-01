"""
input = [[1,4,5],[1,3,4],[2,6]]
output = 1 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

Merging takes O(kN) time where N is the total number of nodes and k is the number of lists.
This is because in the wors case, we'd have k lists with the first list being approx. N length and remaining lists consisting
of one node with an element greater than all others in the list into which we are merging.

This approach takes O(1) space as we will merge the lists into a new list using only one extra node.

1 -> 4 -> 5
1 -> 3 -> 4

next_node => min(node1.val, node2.val)
increment pointer of corresponding node (node = node.next_node).

output = 1 -> 1 -> 3 -> 4 -> 4 -> 5
then merge this with 2 -> 6

Follow up:
    - How can we improve the time complexity?

If we avoid redundantly merging into the biggest list, we can greatly reduce the time complexity to O(Nlogk).
This is because we are instead only merging a total of logk times (as shown below).


"""

class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def merge_lists(lists):

    def merge_two_lists(m, n):
        dummy = top = Node(None)

        while m or n:
            if not m:
                top.next_node = n
                break
            elif not n:
                top.next_node = m
                break

            if m.val <= n.val:
                top.next_node = m
                m = m.next_node
            else:
                top.next_node = n
                n = n.next_node

            top = top.next_node

        return dummy.next_node


    curr = lists[0]
    for idx in range(1, len(lists)):
        curr = merge_two_lists(curr, lists[idx])

    return curr

def merge_lists(lists):

    def merge_two_lists(m, n):
        dummy = top = Node(None)

        while m or n:
            if not m:
                top.next_node = n
                break
            elif not n:
                top.next_node = m
                break

            if m.val <= n.val:
                top.next_node = m
                m = m.next_node
            else:
                top.next_node = n
                n = n.next_node

            top = top.next_node

        return dummy.next_node


    # On first iteration, we merge each adjacent list into 2N/k length lists.
    # On the second iteration, we merge every second list into 4N/k length lists.
    # On the third iteration, we merge every 4th list into 8N/k length lists.
    # And we continue merging each list logk times (as we multiply the interval by 2 each time).
    # This leads to a O(Nlogk) time solution as we are only merging a total of logk times.
    interval = 1
    while interval < len(lists):
        for idx in range(0, len(lists) - interval, interval * 2):
            lists[idx] = merge_two_lists(lists[idx], lists[idx + interval])

        interval *= 2

    return lists[0]

# Recursive solution.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.merge_two_lists(lists[0], lists[1])

        # (0, 1), (2, 3), (4, 5) etc for interval = 1
        # (0, 2), (4, 6), (8, 10) for interval = 2
        # (0, 4), (8, 12), (16, 20) etc. for interval = 4
        # O(NlogL) where L is number of lists and N is total number of nodes in all lists.
        # O(1) space
        #interval = 1
        #while interval < len(lists):
        #    for idx in range(0, len(lists) - interval, 2 * interval):
        #        lists[idx] = merge_two_lists(lists[idx], lists[idx + interval])
        #
        #    interval *= 2


        mid = len(lists) // 2
        return self.mergeKLists([self.mergeKLists(lists[:mid]),
                                 self.mergeKLists(lists[mid:])])

    # O(N) time where N is the number of nodes in a and b.
    def merge_two_lists(self, a, b):

        dummy = top = ListNode(0)
        while a or b:
            if not a:
                top.next = b
                b = None
            elif not b:
                top.next = a
                a = None
            elif a.val <= b.val:
                top.next = a
                a = a.next
            else:
                top.next = b
                b = b.next

            top = top.next

        return dummy.next
