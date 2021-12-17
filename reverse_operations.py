import math
# Add any extra import statements you may need here


class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

  def __repr__(self):
    return f"Node(data={self.data})"

# Add any helper functions you may need here
def reverse_list(head):

  tail = head
  top = None

  while head:
    temp = head
    head = head.next

    temp.next = top
    top = temp

  return top, tail


def reverse(head):
  if not head:
    return

  # Create a dummy node that will be the top node that doesn't move.
  dummy = top = Node(None)
  top.next = head

  # O(N) time where N is number of nodes in linked list.
  # Once we reverse, we continue on from the end of the reversed list so we would have
  # 2 full scans of the list at most.
  # O(1) space.
  while top:
    # If head is odd, advance until the next node is even. Otherwise, continue with below.
    while top.next and top.next.data % 2:
      top = top.next

    # If we reach the end of the list and there is nothing to reverse, return the original head.
    if not top.next:
      return dummy.next

    # Create a temp variable for the start of the reversed list.
    curr = tail = top.next
    # Then set the next node pointer on the current node to None.
    top.next = None

    # Iterate through the reversed list until you reach the end or the next node is odd.
    while tail.next and not tail.next.data % 2:
      tail = tail.next

    # Save a pointer to the next node as end.
    end = tail.next
    tail.next = None

    # Reverse the list using the temp variable and return the new head and tail.
    new_head, new_tail = reverse_list(curr)
    top.next = new_head
    new_tail.next = end

    top = end

  return dummy.next





# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printLinkedList(head):
  print('[', end='')
  while head != None:
    print(head.data, end='')
    head = head.next
    if head != None:
      print(' ', end='')
  print(']', end='')

test_case_number = 1

def check(expectedHead, outputHead):
  global test_case_number
  tempExpectedHead = expectedHead
  tempOutputHead = outputHead
  result = True
  while expectedHead != None and outputHead != None:
    result &= (expectedHead.data == outputHead.data)
    expectedHead = expectedHead.next
    outputHead = outputHead.next

  if not(outputHead == None and expectedHead == None):
    result = False

  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printLinkedList(tempExpectedHead)
    print(' Your output: ', end='')
    printLinkedList(tempOutputHead)
    print()
  test_case_number += 1

def createLinkedList(arr):
  head = None
  tempHead = head
  for v in arr:
    if head == None:
      head = Node(v)
      tempHead = head
    else:
      head.next = Node(v)
      head = head.next
  return tempHead

if __name__ == "__main__":
  head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
  expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
  output_1 = reverse(head_1)
  check(expected_1, output_1)

  head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
  expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])
  output_2 = reverse(head_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
