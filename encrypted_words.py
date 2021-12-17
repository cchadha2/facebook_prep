import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findEncryptedWord(s):
  # Write your code here

  # O(N) time where N is length of s as each character is only visited once
  # and constant time work is done at each char.
  # O(logN) space at most as we are dividing the substring by 2 on each call.
  def generate_encrypted(start, end):
    if start > end:
      return
    elif start == end:
      yield s[start]
      return


    mid = (start + end) // 2
    yield s[mid]
    yield from generate_encrypted(start, mid - 1)
    yield from generate_encrypted(mid + 1, end)


  return "".join(generate_encrypted(0, len(s) - 1))







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
  s1 = "abc"
  expected_1 = "bac"
  output_1 = findEncryptedWord(s1)
  check(expected_1, output_1)

  s2 = "abcd"
  expected_2 = "bacd"
  output_2 = findEncryptedWord(s2)
  check(expected_2, output_2)

  # Add your own test cases here
