from src.sorting import bubble_sort, counting_sort, radix_sort
from src.core.errors import EmptyError

import pytest

test_cases = (
    "input_arr, sorted_arr",
    [
        ([], []),
        ([1], [1]),
        ([3, 2, 1], [1, 2, 3]),
        ([5, 5, 5], [5, 5, 5]),
        ([2, 3, 2, 1], [1, 2, 2, 3]),
        ([1, 2, 10], [1, 2, 10]),
        ([7, 9, 8], [7, 8, 9]),
        ([100, 50, 75], [50, 75, 100]),
        ([0, 1000000], [0, 1000000]),
        ([3, 3, 3, 0], [0, 3, 3, 3]),
        ([10, 0, 10, 0, 10], [0, 0, 10, 10, 10]),
        
        ([-1, 0, 5, -2], [-2, -1, 0, 5]),
        ([-100, -50, -75], [-100, -75, -50]),
        ([-5, 5], [-5, 5]),
    ],
)

@pytest.mark.parametrize(*test_cases)
def test_bubble_sort(input_arr, sorted_arr):
    assert bubble_sort(input_arr) == sorted_arr


@pytest.mark.parametrize(*test_cases)
def test_counting_sort(input_arr, sorted_arr):
    assert counting_sort(input_arr) == sorted_arr

radix_test_cases = (
    "input_arr, sorted_arr",
    test_cases[:-3]
)

@pytest.mark.parametrize(*radix_test_cases)
def test_radix_sort(input_arr, sorted_arr):
    assert radix_sort(input_arr) == sorted_arr