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

    # parser.add_argument('-w', '--wordsGuessed', type=str,
    #                     nargs='+', help='Words that have been guessed')
    args = parser.parse_args()
    return args


def get_allowed_words(bank: list[str], regex: str, include: list[str], exclude: list[str]):
    bank = [w for w in bank if re.search(regex, w)]
    bank = [w for w in bank if all([char in w for char in include])]
    bank = [w for w in bank if all([char not in w for char in exclude])]

    return bank


def main():
    args = get_args()
    words = load()
    allowed = get_allowed_words(words, args.regex, args.include, args.exclude)
    print(", ".join(allowed))
    print(f"{len(allowed)}/{len(words)}")


if __name__ == '__main__':
    main()
