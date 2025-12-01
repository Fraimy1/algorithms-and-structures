from src.algorithms.factorial_fibo import factorial, factorial_recursive, fibo, fibo_recursive
from src.core.errors import NegativeNumberError

import pytest  # type: ignore[import-not-found]

@pytest.mark.parametrize("n, result", [
    (1, 1),
    (0, 1),
    (5, 120),
    (4, 24)
])
def test_factorial_function(n, result):
    actual_output = factorial(n)
    assert actual_output == result


def test_factorial_negative_number():
    with pytest.raises(NegativeNumberError):
        factorial(-1)


@pytest.mark.parametrize("n, result", [
    (1, 1),
    (0, 1),
    (5, 120),
    (4, 24)
])
def test_recursive_factorial_function(n, result):
    actual_output = factorial_recursive(n)
    assert actual_output == result


def test_recursive_factorial_negative_number():
    with pytest.raises(NegativeNumberError):
        factorial_recursive(-1)


@pytest.mark.parametrize("n, result", [
    (1, 1),
    (0, 0),
    (5, 5),
    (4, 3),
    (10, 55)
])
def test_fibonacci_function(n, result):
    actual_output = fibo(n)
    assert actual_output == result

@pytest.mark.parametrize("n, result", [
    (1, 1),
    (0, 0),
    (5, 5),
    (4, 3),
    (10, 55)
])
def test_fibonacci_recursive(n, result):
    actual_output = fibo_recursive(n)
    assert actual_output == result
