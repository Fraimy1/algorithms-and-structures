from src.sorting.linear import bucket_sort, counting_sort, radix_sort
from src.sorting.comparison import bubble_sort, heap_sort, quick_sort
from src.core.errors import NegativeNumberError

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
    test_cases[0],
    test_cases[1][:-3]
)

@pytest.mark.parametrize(*radix_test_cases)
def test_radix_sort(input_arr, sorted_arr):
    assert radix_sort(input_arr) == sorted_arr


@pytest.mark.parametrize("input_arr", [
    [-1, 0, 5, -2],
    [-100, -50, -75],
    [-5, 5],
    [-1],
])
def test_radix_sort_negative_numbers(input_arr):
    with pytest.raises(NegativeNumberError):
        radix_sort(input_arr)


bucket_test_cases = (
    "input_arr, sorted_arr",
    [
        ([], []),
        ([0.0], [0.0]),
        ([0.1, 0.2, 0.3], [0.1, 0.2, 0.3]),
        ([0.3, 0.2, 0.1], [0.1, 0.2, 0.3]),
        ([0.12, 0.87, 0.33, 0.29, 0.01],
         [0.01, 0.12, 0.29, 0.33, 0.87]),
        ([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
        ([0.99, 0.01, 0.5, 0.25, 0.75],
         [0.01, 0.25, 0.5, 0.75, 0.99]),
        ([0.19, 0.21, 0.2], [0.19, 0.2, 0.21]),
    ],
)

@pytest.mark.parametrize(*bucket_test_cases)
def test_bucket_sort(input_arr, sorted_arr):
    assert bucket_sort(input_arr) == sorted_arr


@pytest.mark.parametrize(*test_cases)
def test_heap_sort(input_arr, sorted_arr):
    assert heap_sort(input_arr) == sorted_arr

@pytest.mark.parametrize(*test_cases)
def test_quick_sort(input_arr, sorted_arr):
    assert quick_sort(input_arr) == sorted_arr
