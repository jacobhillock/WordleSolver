# Standard Libraries
from sys import exit
from argparse import ArgumentParser, Namespace

# Custom Imports
from Custom_Exceptions import LetterException, LoadException, FormatException
from globals import WORD_LENGTH
from process_words import process_guessed_words
from load_words import load
from allowed_words import get_allowed_words
from score import score


def get_args() -> Namespace:
    parser = ArgumentParser(description='Description.')
    parser.add_argument('-a', '--allWords', action='store_true')
    parser.add_argument('-w', '--wordsGuessed', type=str,
                        nargs='+', help="""Words that have been guessed with the following format
                        xx[a]xx: a is in the correct spot
                        xx{a}xx: a exists in the word
                        xxaxx: a does not exist in the word""")
    args = parser.parse_args()
    return args


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

    allowed = words
    if (not args.allWords):
        # print("\n".join([f"{key}: {value}" for key, value in include.items()]))
        allowed = get_allowed_words(words, regex, include, exclude)
    scored = score(allowed)
    print(", ".join(scored))
    print(f"{len(allowed)}/{len(words)}")


if __name__ == '__main__':
    main()
