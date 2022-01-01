import re
import string

class Solution:
    def isNumber(self, s: str) -> bool:
        """Overall O(N) time and space."""


        # First char can be +, -, ., or a number but can't be an e or E
        # Second char cannot be a + or a -
        # . must come before e or E

        # O(N) time and O(1) space.
        def check_integer(num):
            has_sign = num[0] == "+" or num[0] == "-"
            has_num = False

            for idx in range(has_sign, len(num)):
                if not num[idx].isdigit():
                    return False

                has_num = True

            return has_num

        # O(N) time and O(1) space.
        def check_decimal(num):
            has_sign = num[0] == "+" or num[0] == "-"
            has_num = decimal = False

            for idx in range(has_sign, len(num)):
                if (num[idx] == "+" or num[idx] == "-"
                    or (num[idx] == "." and decimal)):
                    return False
                elif num[idx] == ".":
                    decimal = True
                    continue
                elif not num[idx].isdigit():
                    return False

                has_num = True

            return has_num

        # O(1) time and O(1) space.
        allowed_chars = set(string.digits)
        allowed_chars.add("+")
        allowed_chars.add("-")
        allowed_chars.add(".")
        if not s[0] in allowed_chars or not s[-1] in allowed_chars:
            return False

        # O(N) time and O(N) space for components list.
        components = re.split(r"[eE]", s, maxsplit=1)
        if not components[0]:
            components = components[1:]
        if not components[-1]:
            components.pop()
        if not 1 <= len(components) < 3:
            return False

        if not check_decimal(components[0]) and not check_integer(components[0]):
            return False

        if len(components) > 1 and not check_integer(components[1]):
            return False

        return True
