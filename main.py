from operator import ge
import sys
import argparse
import re


def load() -> list[str]:
    data = []
    with open('words', 'r') as file:
        data = file.read().split('\n')
    if (len(data) == 0):
        print('No words list, please read README.md')
        sys.exit(-1)
    return data


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Description.')
    parser.add_argument('-r', '--regex', type=str,
                        help='Regex pattern to find')
    parser.add_argument('-e', '--exclude', type=str, nargs='*',
                        help='Letters that can not be included')
    parser.add_argument('-i', '--include', type=str, nargs='*',
                        help='Letters needed to be included')

    parser.add_argument('-w', '--wordsGuessed', type=str,
                        nargs='+', help="""Words that have been guessed with the following format
                        xx[a]xx: a is in the correct spot
                        xx{a}xx: a exists in the word
                        xxaxx: a does not exist in the word""")
    args = parser.parse_args()
    return args


def get_allowed_words(bank: list[str], regex: str, include: list[str], exclude: list[str]):
    bank = [w for w in bank if re.search(regex, w)]
    bank = [w for w in bank if all([char in w for char in include])]
    bank = [w for w in bank if all([char not in w for char in exclude])]

    return bank


def process_guessed_words(words_guessed: list[str]):
    include = []
    exclude = []
    regex_list = ['.', '.', '.', '.', '.']

    for word in words_guessed:
        letters = re.findall("\w", word)
        word_t = word
        print(letters)
        for letterPos, letter in enumerate(letters):
            print(word_t)
            i = word_t.index(letter)
            if i == 0:
                if letter not in include:
                    if (type(regex_list[letterPos]) != list and regex_list[letterPos] == '.'):
                        regex_list[letterPos] = list([])
                    if (type(regex_list[letterPos]) == list):
                        regex_list[letterPos].append(letter)
                        exclude.append(letter)
                word_t = word_t[1:]
            elif word_t[i-1] == '[' and word_t[i+1] == ']':
                include.append(letter)
                regex_list[letterPos] = letter
                word_t = word_t[3:]
            elif word_t[i-1] == '{' and word_t[i+1] == '}':
                include.append(letter)
                if (type(regex_list[letterPos]) != list and regex_list[letterPos] == '.'):
                    regex_list[letterPos] = list([])
                regex_list[letterPos].append(letter)
                word_t = word_t[3:]

    regex = ""
    for r in regex_list:
        if type(r) == list:
            regex += '[^' + "".join(r) + ']'
        else:
            regex += r
    exclude = [e for e in exclude if e not in include]
    # print(regex, include, exclude)
    return regex, include, exclude


def main():
    args = get_args()
    if (args.wordsGuessed is not None):
        args.regex, args.include, args.exclude = process_guessed_words(
            args.wordsGuessed)
    words = load()
    allowed = get_allowed_words(words, args.regex, args.include, args.exclude)
    print(", ".join(allowed))
    print(f"{len(allowed)}/{len(words)}")


if __name__ == '__main__':
    main()
