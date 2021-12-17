def validate_abbr(word, abbr):

    word_idx = len(word) - 1
    abbr_idx = len(abbr) - 1

    while word_idx >= 0 and abbr_idx >= 0:
        if abbr[abbr_idx].isdigit():
            order = curr = 0
            while abbr_idx >= 0 and abbr[abbr_idx].isdigit():
                curr += int(abbr[abbr_idx]) * (10 ** order)
                abbr_idx -= 1
                order += 1

            if abbr[abbr_idx + 1] == "0":
                return False
            word_idx -= curr
        else:
            if not word[word_idx] == abbr[abbr_idx]:
                return False

            word_idx -= 1
            abbr_idx -= 1

    return word_idx < 0 and word_idx == abbr_idx
