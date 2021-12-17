import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getBillionUsersDay(growthRates):
  # Write your code here

  # O(N) time and space.
  state = growthRates.copy()
  total = sum(growthRates)

  days = 1
  limit = 10**9
  # O(10_000_000_000 / growth at each step)
  while total < limit:

    days += 1

    curr = 0
    # O(N) time.
    for idx, value in enumerate(growthRates):
      state[idx] *= value
      curr += state[idx]

      if curr >= limit:
        return days

    total = curr

  return days


          
def getBillionUsersDay(growthRates):

  limit = 10**9
  start, end = 1, 5000

  # O(logN) time where N is 5000 at most (good guess?).
  # O(1) space.
  while start <= end:
    mid = (start + end) // 2
    guess = sum(growthRate ** mid for growthRate in growthRates)

    if guess > limit:
      end = mid - 1
    else:
      start = mid + 1

  return mid


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
  test_1 = [1.1, 1.2, 1.3]
  expected_1 = 79
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)

  test_2 = [1.01, 1.02]
  expected_2 = 1047
  output_2 = getBillionUsersDay(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
