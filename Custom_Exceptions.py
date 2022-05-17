class LoadException (Exception):
    def __init__(self, *args):
        if args:
            self.message = " ".join(args)
        else:
            self.message = "Failed to load file"

    def __str__(self):
        return self.message


class LetterException (Exception):
    def __init__(self, *args):
        if args:
            self.message = " ".join(args)
        else:
            self.message = f"Word length was not {WORD_LENGTH}"

    def __str__(self):
        return self.message


class FormatException (Exception):
    def __init__(self, *args):
        if args:
            self.message = " ".join(args)
        else:
            self.message = "Invalid Format"

    def __str__(self):
        return self.message
