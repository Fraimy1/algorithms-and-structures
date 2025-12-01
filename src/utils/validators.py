# src/utils/validators.py

from src.core.errors import IncorrectInputError
from src.core.logging import log_and_raise
class GeneratorValidator:

    @staticmethod
    def check_rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed=None) -> list|None:
        if n < 0:
            log_and_raise(IncorrectInputError(f"n must be non-negative. But recieved n = {n}"))
        if lo > hi:
            log_and_raise(IncorrectInputError(f"lo <= hi required. But recieved lo = {lo} > hi = {hi}"))
        if distinct and hi - lo + 1 < n:
            log_and_raise(IncorrectInputError(f"range too small for distinct values. But recieved {hi - lo + 1} < n = {n}"))
        if n == 0:
            return []
        return None

    @staticmethod
    def check_nearly_sorted(n: int, swaps: int, *, seed=None) -> list|None:
        if n < 0:
            log_and_raise(IncorrectInputError(f"n must be non-negative. But recieved n = {n}"))
        if swaps < 0:
            log_and_raise(IncorrectInputError(f"swaps must be non-negative. But recieved swaps = {swaps}"))
        if swaps > n:
            log_and_raise(IncorrectInputError(f"swaps must be less than or equal to n. But recieved swaps = {swaps} > n = {n}"))
        if n == 0:
            return []
        return None

    @staticmethod
    def check_many_duplicates(n: int, k_unique: int, *, seed=None) -> list|None:
        if n < 0:
            log_and_raise(IncorrectInputError(f"n must be non-negative. But recieved n = {n}"))
        if k_unique > n:
            log_and_raise(IncorrectInputError(f"k_unique must be less than or equal to n. But recieved k_unique = {k_unique} > n = {n}"))
        if n == 0:
            return []
        return None

    @staticmethod
    def check_reverse_sorted(n: int) -> list|None:
        if n < 0:
            log_and_raise(IncorrectInputError(f"n must be non-negative. But recieved n = {n}"))
        if n == 0:
            return []
        return None

    @staticmethod
    def check_rand_float_array(n: int, lo: float, hi: float, *, seed=None) -> list|None:
        if n < 0:
            log_and_raise(IncorrectInputError(f"n must be non-negative. But recieved n = {n}"))
        if lo > hi:
            log_and_raise(IncorrectInputError(f"lo <= hi required. But recieved lo = {lo} > hi = {hi}"))
        if n == 0:
            return []
        return None
