import math
# Add any extra import statements you may need here
from collections import Counter

# Add any helper functions you may need here


def min_length_substring(s, t):
  if s == t:
    return 1
  elif len(s) == len(t):
    return len(s) if Counter(s) == Counter(t) else -1

  # Write your code here

  # O(n) space.
  count_s = Counter()
  count_t = Counter(t)

  start, end = 0, 1
  window = math.inf
  count_s[s[0]] += 1

  # O(nm) time as we do at most 2 scans of s (of length n) and for each iteration,
  # there is an O(m) time call to check both counters.
  while end < len(s):

    count_s[s[end]] += 1

    # O(min(m, n)) time.
    if count_t & count_s == count_t:

      while start < end and count_t & count_s == count_t:
        count_s[s[start]] -= 1
        start += 1

      window = min(window, end - start + 2)

    end += 1

  return window if window != math.inf else -1











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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  check(-1, min_length_substring("kjficjalfl", "kjgicnaxfl"))
