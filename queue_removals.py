import math
# Add any extra import statements you may need here
from collections import deque

# Add any helper functions you may need here


def findPositions(arr, x):
  # Write your code here

  queue = deque(([val, idx + 1] for idx, val in enumerate(arr)))
  inter_queue = deque()
  output = []

  # n <= x*x.
  # Overall O(x^2) time and O(N) space for the queue.
  # O(x) time.
  for _ in range(x):

    maximum = None
    # O(x) time.
    for _ in range(x):
      if not queue:
        break

      pair = queue.popleft()

      if not maximum or maximum[0] < pair[0]:
        maximum = pair

      inter_queue.append(pair)

    output.append(maximum[1])

    # O(x) time.
    while inter_queue:
      pair = inter_queue.popleft()

      if pair == maximum:
        continue

      if pair[0] > 0:
        pair[0] -= 1

      queue.append(pair)

  return output





# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 6
  x_1 = 5
  arr_1 = [1, 2, 2, 3, 4, 5]
  expected_1 = [5, 6, 4, 1, 2]
  output_1 = findPositions(arr_1, x_1)
  check(expected_1, output_1)

  n_2 = 13
  x_2 = 4
  arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
  expected_2 = [2, 5, 10, 13]
  output_2 = findPositions(arr_2, x_2)
  check(expected_2, output_2)

  # Add your own test cases here
