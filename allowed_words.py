from re import search, findall


class AllowedStructure:
    def __init__(self, amount, strict=False) -> None:
        self.amount = amount
        self.strict = strict

    def __add__(self, plus: int) -> None:
        self.amount += plus
        return self

    def __str__(self) -> str:
        return f"amount: {self.amount}; strict: {self.strict}"

    def eval(self, amount) -> bool:
        if self.strict:
            return amount == self.amount
        else:
            return amount >= self.amount

    def is_strict(self) -> None:
        self.strict = True


def include_word(word: str, char: str, count: AllowedStructure) -> bool:
    finds = findall(char, word)
    return count.eval(len(finds))


def get_allowed_words(bank: list[str], regex: str, include: dict[str, AllowedStructure], exclude: list[str]) -> list[str]:
    bank = [w for w in bank if search(regex, w)]
    bank = [w for w in bank if all(
        [include_word(w, char, count) for char, count in include.items()])]
    bank = [w for w in bank if all([char not in w for char in exclude])]

    return bank
