from Custom_Exceptions import LoadException


def load() -> list[str]:
    data = []
    with open('words', 'r') as file:
        data = file.read().split('\n')
    if (len(data) == 0):
        raise LoadException('No words list, please read README.md')
    return data
