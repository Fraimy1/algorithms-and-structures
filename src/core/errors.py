class CustomError(Exception):
    def __init__(self, message: str):
        self.message = message

class NegativeNumberError(CustomError):
    pass

class IncorrectInputError(CustomError):
    pass

class EmptyError(CustomError):
    pass

class OutOfRangeError(CustomError):
    pass
