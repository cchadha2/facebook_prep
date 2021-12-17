import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def balancedSplitExists(arr):
  # Write your code here

  # [9, 1, 2, 3, 6, 3, 4, 5]
  # [1, 2, 3, 3, 4, 5, 6, 9]
  # left = [1, 3, 6, 9, 13, 18, 24, 33]
  # right = [33, 32, 30, 27, 24, 20, 15, 9]
  # No split possible as there are no two adjacent equal sums.

  # [12, 7, 6, 7, 6]
  # [6, 6, 7, 7, 12]
  # left = [6, 12, 19, 26, 38]
  # right = [38, 32, 26, 19, 12]
  # two adjacent equal sums but the numbers in the indices are equal so false.

  # [1, 5, 7, 1]
  # [1, 1, 5, 7]
  # sums = [1, 2, 7, 14]
  # right = [14, 13, 12, 7]

  # O(NlogN) overall and O(N) space.
  arr.sort()

  # O(N) time
  sums = [0] * len(arr)
  sums[0] = arr[0]
  for idx in range(1, len(arr)):
    sums[idx] = sums[idx - 1] + arr[idx]

  # O(N) time.
  # From the right.
  curr = arr[-1]
  for idx in range(len(arr) - 2, 0, -1):
    if curr == sums[idx] and arr[idx] < arr[idx + 1]:
      return True

    curr += sums[idx]

  return False











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1, 2, 5]
  expected_1 = True
  output_1 = balancedSplitExists(arr_1)
  check(expected_1, output_1)

  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  arr_3 = [9, 1, 2, 3, 6, 3, 4, 5]
  expected_3 = False
  output_3 = balancedSplitExists(arr_3)
  check(expected_3, output_3)
