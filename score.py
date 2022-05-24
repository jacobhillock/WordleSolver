from math import comb
from re import findall
from load_words import load

ALL_LETTERS = findall('[a-z]', 'abcdefghijklmnopqrstuvwxyz')


def get_overall_frequency() -> dict[str, float]:
    freq_table = {}
    bank = load()
    combine_bank = ''.join(bank).lower()
    for letter in combine_bank:
        freq_table[letter] = freq_table.get(letter, 0) + 1

    for key, item in freq_table.items():
        freq_table[key] = item / len(combine_bank)

    return freq_table


def get_sorted_words(word_score: dict[str, float]) -> list[str]:
    data = reversed(sorted(word_score.items(), key=lambda x: x[1]))
    words = [item[0] for item in data]
    return words


def score(list: list[str]) -> list[str]:
    table = get_overall_frequency()
    word_score = {}
    for word in list:
        for letter in set(word):
            word_score[word] = word_score.get(word, 0) + table[letter]

    return get_sorted_words(word_score)


if __name__ == '__main__':
    print(score(['words', 'manor', 'salet', 'table', 'eaves']))
