from src.core.errors import NegativeNumberError
from src.core.logging import log_and_raise

def factorial(n: int) -> int:
    if n < 0:
        log_and_raise(NegativeNumberError("Factorial is not defined for negative numbers"))

    res = 1
    for i in range(2, n+1):
        res *= i
    return res


def factorial_recursive(n: int) -> int:
    if n < 0:
        log_and_raise(NegativeNumberError("Factorial is not defined for negative numbers"))

    if n == 0:
        return 1

    def _fact(i: int, result: int) -> int:
        if i == n+1:
            return result

        return _fact(i = i+1, result = result*i)

    return _fact(1, 1)


def fibo(n: int) -> int:
    if n < 0:
        log_and_raise(NegativeNumberError("Fibonacci is not defined for negative numbers"))

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev_2_nums = [0, 1]

    for i in range(2, n+1):
        sum_of_2_nums = sum(prev_2_nums)
        prev_2_nums[0] = prev_2_nums[1]
        prev_2_nums[1] = sum_of_2_nums

    return prev_2_nums[1]


def fibo_recursive(n: int) -> int:
    if n < 0:
        log_and_raise(NegativeNumberError("Fibonacci is not defined for negative numbers"))
    if n == 0:
        return 0
    if n == 1:
        return 1

    def _fibo(a: int, b: int, i: int) -> int:
        if n==i:
            return b

        return _fibo(b, a+b, i+1)

    return _fibo(0, 1, 1)
