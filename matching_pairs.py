import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
  # Write your code here

  # O(N) space  where N is length of s.
  not_equal = []

  # O(N) time.
  equal = 0
  for idx in range(len(s)):
    if s[idx] == t[idx]:
      equal += 1
    else:
      not_equal.append((s[idx], t[idx]))

  if not not_equal:
    return equal - 2

  max_swap = 0
  # O(N^2) time.
  for idx, pair in enumerate(not_equal):
    for other_pair in not_equal[idx + 1 :]:
      if pair[1] == other_pair[0]:
        max_swap = 1

        if pair[0] == other_pair[1]:
          return equal + 2

  return equal + max_swap











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
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  check(3, matching_pairs("abcd", "adcc"))

  check(0, matching_pairs("fhif", "adcc"))
