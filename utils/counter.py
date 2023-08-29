def count_single_chars(char, counter):
    if not char.isalnum() and not char.isspace():
        counter[char] += 1


def count_bigrams(char, last_char, counter):
    if char.isalnum() or char.isspace():
        return None

    if last_char is not None:
        counter[f"{last_char}{char}"] += 1

    return char
