import math
# Add any extra import statements you may need here
import heapq

# Add any helper functions you may need here


def minOverallAwkwardness(arr):
  # Write your code here

  # To improve on this, we can add the negative of the
  # heights to a heap and pop the largest each time finding
  # the awkwardness between the two popped and the last two popped.
  # At the end, we find the awkwardness between the last two themselves
  # as well (for the 0 -> N - 1 indexes). This would avoid creating the
  # extra arrangement array (though we still need O(N) space for the heap itself).
  # It would also avoid the extra O(N) iteration to find the maximum awkwardness.


  # [5, 1, 6, 8, 10, 15]
  # [1, 5, 6, 8, 10, 15] => 14 awkwardness
  # reverse first half of array:
  # [8, 6, 5, 1, 10, 15] => 8 awkwardness

  # [1, 5, 10, 15, 8, 6] => [8, 6, 1, 5, 10, 15]

  # O(N) time and O(N) extra space for arrangement array.
  heapq.heapify(arr)
  arrangement = [None] * len(arr)
  start, end = 0, len(arr) - 1

  # O(NlogN) time to pop all items from the heap.
  while start <= end:
    if arr:
      arrangement[start] = heapq.heappop(arr)

    if arr:
      arrangement[end] = heapq.heappop(arr)

    start += 1
    end -= 1

  # O(N) time to find the overall awkwardness in the arrangement.
  maximum = abs(arrangement[0] - arrangement[-1])
  for idx in range(len(arrangement) - 1):
    maximum = max(maximum, abs(arrangement[idx] - arrangement[idx + 1]))

  return maximum










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [5, 10, 6, 8]
  expected_1 = 4
  output_1 = minOverallAwkwardness(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2, 5, 3, 7]
  expected_2 = 4
  output_2 = minOverallAwkwardness(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
