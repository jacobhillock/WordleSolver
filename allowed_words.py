from re import search, findall


def include_word(word: str, char: str, count: int) -> bool:
    finds = findall(char, word)
    return len(finds) == count


def get_allowed_words(bank: list[str], regex: str, include: dict[str, int], exclude: list[str]):
    bank = [w for w in bank if search(regex, w)]
    bank = [w for w in bank if all(
        [include_word(w, char, count) for char, count in include.items()])]
    bank = [w for w in bank if all([char not in w for char in exclude])]

    return bank
