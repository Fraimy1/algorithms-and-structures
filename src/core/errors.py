class NegativeNumberError(Exception):
    def __init__(self, message: str):
        self.message = message

class IncorrectInputError(Exception):
    def __init__(self, message: str):
        self.message = message

class EmptyError(Exception):
    def __init__(self, message: str):
        self.message = message

class OutOfRangeError(Exception):
    def __init__(self, message: str):
        self.message = message