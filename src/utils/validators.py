# src/utils/validators.py

from typing import Callable
from src.core.errors import IncorrectInputError

class BoundsValidator:
    def __init__(self, check_distinct: bool = False):
        self.check_distinct = check_distinct

    def __call__(self, func: Callable) -> Callable:
        def wrapper(n: int, lo: int, hi: int, *args, distinct: bool = False, **kwargs) -> list[int]:
            if n < 0:
                raise IncorrectInputError(f"n must be non-negative. But recieved n = {n}")
            if lo > hi:
                raise IncorrectInputError(f"lo <= hi required. But recieved lo = {lo} > hi = {hi}")
            if self.check_distinct and distinct:
                if hi - lo + 1 < n:
                    raise IncorrectInputError(f"range too small for distinct values. But recieved {hi - lo + 1} < n = {n}")

            return func(n, lo, hi, *args, distinct=distinct, **kwargs)
        return wrapper