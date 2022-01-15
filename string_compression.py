class Solution:
    def compress(self, chars: List[str]) -> int:

        def append_char(idx, char, count):
            chars[idx] = curr_char
            idx += 1
            if count > 1:
                # O(1) time and space as we know the maximum count is 2000.
                # Otherwise, would be O(N) time and space.
                for count_char in str(count):
                    chars[idx] = count_char
                    idx += 1

            return idx

        last_char_idx = count = 0
        curr_char = chars
        # O(N) time where N is number of chars and O(1) space. But could also
        # be said to be O(1) time as maximum length of chars is specified.
        for idx, char in enumerate(chars):
            if curr_char is None:
                curr_char = char
            if char == curr_char:
                count += 1

            if char != curr_char:
                last_char_idx = append_char(last_char_idx,
                                            curr_char,
                                            count)

                curr_char = char
                count = 1

            if idx == (len(chars) - 1):
                last_char_idx = append_char(last_char_idx,
                                            curr_char,
                                            count)

        while len(chars) > last_char_idx:
            chars.pop()
