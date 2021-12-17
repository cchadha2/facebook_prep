import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getTotalTime(arr):
  # Write your code here

  # [2, 3, 9, 8, 4]

  # After sorting: [2, 3, 4, 8, 9]

  # 8 + 9 = 17, penalty = 17
  # 17 + 4 = 21, penalty = 17 + 21 = 38
  # 21 + 3 = 24, penalty = 38 + 24 = 62
  # 24 + 2 = 26, penalty = 62 + 26 = 88

  # Because all numbers are positive, we're best off adding all the biggest numbers together.

  # O(NlogN) time and O(N) space at worst for sort.
  arr.sort(reverse=True)
  penalty = 0
  curr = arr[0]

  # O(N) time.
  for idx in range(1, len(arr)):
    curr += arr[idx]
    penalty += curr

  return penalty







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
  arr_1 = [4, 2, 1, 3]
  expected_1 = 26
  output_1 = getTotalTime(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 3, 9, 8, 4]
  expected_2 = 88
  output_2 = getTotalTime(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  arr_2 = [2]
  expected_2 = 0
  output_2 = getTotalTime(arr_2)
  check(expected_2, output_2)
