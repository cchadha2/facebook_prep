# O(N) time and O(1) space solution for two pointers.
def valid_palindrome(s):

    def check_indices(start, end, deleted):
        while start < end:
            if not s[start] == s[end]:
                if deleted:
                    return False
                else:
                    return (check_indices(start + 1, end, True)
                            or check_indices(start, end - 1, True))

            start += 1
            end -= 1

        return True

    return check_indices(0, len(s) - 1, False)


s = "abca"
exp = True
print(valid_palindrome(s) == exp)


s = "aba"
exp = True
print(valid_palindrome(s) == exp)

s = "ab"
exp = True
print(valid_palindrome(s) == exp)

s = "aabac"
exp = False
print(valid_palindrome(s) == exp)
