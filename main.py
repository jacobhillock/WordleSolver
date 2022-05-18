# Standard Libraries
from operator import ge
from sys import exit
from argparse import ArgumentParser, Namespace
from re import search, findall

# Custom Imports
from Custom_Exceptions import LetterException, LoadException, FormatException
from process_words import process_guessed_words
from load_words import load
from globals import WORD_LENGTH


def get_args() -> Namespace:
    parser = ArgumentParser(description='Description.')

    parser.add_argument('-w', '--wordsGuessed', type=str,
                        nargs='+', help="""Words that have been guessed with the following format
                        xx[a]xx: a is in the correct spot
                        xx{a}xx: a exists in the word
                        xxaxx: a does not exist in the word""")
    args = parser.parse_args()
    return args


def include_word(word: str, char: str, count: int) -> bool:
    finds = findall(char, word)
    return len(finds) == count


def get_allowed_words(bank: list[str], regex: str, include: dict[str, int], exclude: list[str]):
    bank = [w for w in bank if search(regex, w)]
    bank = [w for w in bank if all(
        [include_word(w, char, count) for char, count in include.items()])]
    bank = [w for w in bank if all([char not in w for char in exclude])]

    return bank


def main():
    args = get_args()
    regex = ""
    include = {}
    exclude = []
    try:
        words = load()
        if (args.wordsGuessed is not None):
            regex, include, exclude = process_guessed_words(
                args.wordsGuessed)
    except LetterException as e:
        print(e)
        exit()
    except FormatException as e:
        print(e)
        exit()
    except LoadException as e:
        print(e)
        exit()

    allowed = get_allowed_words(words, regex, include, exclude)
    print(", ".join(allowed))
    print(f"{len(allowed)}/{len(words)}")


if __name__ == '__main__':
    main()
