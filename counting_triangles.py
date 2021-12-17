import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def countDistinctTriangles(arr):
  # Write your code here

  # O(N * 3log3) = O(N)
  for idx, triangle in enumerate(arr):
    arr[idx] = sorted(triangle)

  # O(NlogN) time and O(N) space at worst.
  arr.sort()

  # O(N) time.
  distinct = 0
  curr = None
  for triangle in arr:
    if not curr or curr != triangle:
      distinct += 1
      curr = triangle

  return distinct



def countDistinctTriangles(arr):

  # O(N) time and space as sort is always on sequence of 3 elements which is O(3log3) = O(1).
  distinct = set()
  for triangle in arr:
    distinct.add(tuple(sorted(triangle)))

  return len(distinct)






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
  arr_1 = [(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]
  expected_1 = 3
  output_1 = countDistinctTriangles(arr_1)
  check(expected_1, output_1)

  arr_2 = [(3, 4, 5), (8, 8, 9), (7, 7, 7)]
  expected_2 = 3
  output_2 = countDistinctTriangles(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  arr_2 = [[5, 8, 9], [5, 9, 8], [9, 5, 8], [9, 8, 5], [8, 9, 5], [8, 5, 9]]
  expected_2 = 1
  output_2 = countDistinctTriangles(arr_2)
  check(expected_2, output_2)

  arr_2 = [[8, 4, 6], [100, 101, 102], [84, 93, 173]]
  expected_2 = 3
  output_2 = countDistinctTriangles(arr_2)
  check(expected_2, output_2)
