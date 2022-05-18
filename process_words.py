from re import findall
from Custom_Exceptions import LetterException, FormatException
from globals import WORD_LENGTH
from typing import Tuple


def process_guessed_words(words_guessed: list[str]) -> Tuple[str, dict[str, int], list[str]]:
    include = {}
    exclude = []
    regex_list = [list([]) for _ in range(WORD_LENGTH)]

    # process words
    for word in words_guessed:
        word_t = word
        run_include = {}
        # find letters in word
        letters = findall("\w", word)

        if len(letters) != WORD_LENGTH:
            raise LetterException(f"{word} is not {WORD_LENGTH} letters")

        # collect data needed for includes/excludes and regex
        for letterPos, letter in enumerate(letters):
            i = word_t.index(letter)
            # letter does not have location noted
            if i == 0:
                # ensure letter was not solved
                if type(regex_list[letterPos]) == list:
                    regex_list[letterPos].append(letter)
                if letter not in run_include.keys():
                    exclude.append(letter)

                word_t = word_t[1:]

            # letter is surrounded by [] meaning it is correct
            elif word_t[i-1] == '[' and word_t[i+1] == ']':
                run_include[letter] = run_include.get(letter, 0) + 1
                regex_list[letterPos] = letter
                word_t = word_t[3:]

            # letter is surrounded by {} meaning it is in word
            elif word_t[i-1] == '{' and word_t[i+1] == '}':
                run_include[letter] = run_include.get(letter, 0) + 1
                if (type(regex_list[letterPos]) == list):
                    regex_list[letterPos].append(letter)
                word_t = word_t[3:]

            # print format error
            else:
                raise FormatException(f"""Input Error: \"{word_t[:3]}\" is not recognized as a valid character type.
                Acceptable types:
                - Correct Location: [a]
                - Incorrect Location: {{a}}
                - Not in word: a
                """)
        for key, count in run_include.items():
            include[key] = count if count > include.get(
                key, 0) else include.get(key, 0)

    # sanitize data
    for i, reg in enumerate(regex_list):
        if type(reg) == list:
            regex_list[i] = [value for value in reg if value not in exclude]
    exclude = [e for e in exclude if e not in include]
    exclude = list(set(exclude))

    # build regex
    regex = ""
    for r in regex_list:
        if type(r) == list:
            if len(r) != 0:
                regex += '[^' + "".join(r) + ']'
            else:
                regex += '.'
        else:
            regex += r
    return regex, include, exclude
