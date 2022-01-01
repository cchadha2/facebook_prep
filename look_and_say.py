"""
The worst case time complexity for look and say is O(2^N).

Take this example (worst-case):

"123123123123123"

which has length 15. This transforms to:

"111213111213111213111213111213"

which has length 30. Thereby, we've doubled our input. The space required for
this implementation is then also O(2^N) for the stack that counts characters.
"""
import math

def look_and_say(n):
    """Overall O(2^N) time and O(2^N) space"""
    if n <= 0:
        return

    # The max value we can get is "3" because if we take the example:
    # "12" -> "1112" -> "3112" -> "132112" -> "1113122112" -> "311311222112"
    # Then we can see that as soon as we get to a group of 3 same digits in a
    # row, the group is squashed to a 3. It is not possible to line up 4 same
    # digits in a row. The only way we could get a "4" is from:
    # "1111" -> "41"
    # "2222" -> "42"
    # "3333" -> "43"
    # However, the first case cannot occur as there as the prior sequence would
    # need to be "1111" -> "1111" which would result in "41" so this is impossible.
    # Similarly for the "2" case, we need "2222" -> "2222" but this would result
    # in "42" so we can't ever reach "2222". For "3333" to occur, we'd need
    # "333333333333" -> "3333" which would actually condense to "123" instead.
    text = "11"
    # Only starting sequence that won't grow in length.
    #text = "22"
    # O(N) time.
    for num in range(1, n + 1):
        print(num, 2**num, len(text))
        print(text)
        stack = []
        curr = None

        # O(2^N) time and space
        for digit in text:
            if not curr:
                curr = digit
                count = 1
            elif digit != curr:
                stack.append((count, curr))
                curr = digit
                count = 1
            else:
                count += 1
        stack.append((count, curr))
        text = "".join(str(count) + digit for count, digit in stack)

look_and_say(15)
