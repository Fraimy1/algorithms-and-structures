# counting, radix, bucket
from src.core.errors import NegativeNumberError
from src.core.errors import OutOfRangeError
from src.core.logging import log_and_raise
from src.sorting.comparison import bubble_sort

def _get_min_max(arr: list[int]) -> tuple[int, int]:
    cur_min, cur_max = 0, 0

    for n in arr:
        if n < cur_min:
            cur_min = n

        if n > cur_max:
            cur_max = n
    return cur_min, cur_max

def counting_sort(arr: list) -> list[int]:

    min_n, max_n = _get_min_max(arr)

    shift = 0
    if min_n < 0:
        shift = abs(min_n)

    min_n, max_n = min_n + shift, max_n + shift

    counts = [0 for _ in range(min_n, max_n+1)]
    for n in arr:
        counts[n+shift] +=1

    return [value-shift for value, count in enumerate(counts, start=min_n) for _ in range(count)]

def flatten(arrays: list[list]) -> list:
    return [el for arr in arrays for el in arr]

def radix_sort(arr: list, base: int = 10) -> list[int]:
    """
    Radix sort only works for positive numbers
    """
    if any(n < 0 for n in arr):
        log_and_raise(NegativeNumberError("Radix sort only works for positive numbers"))

    if not arr:
        return arr

    if len(arr) ==1:
        return arr

    buckets: list[list[int]] = [[] for _ in range(base)]

    max_n = max(arr)
    n_digits = len(str(abs(max_n)))

    for i in range(n_digits):
        # i = i digits from the end
        # e.g. 1 is tens, 2 is 100s etc.

        for n in arr:
            # get the i last digit of n
            # digit = int(str(abs(n))[-(i+1)])
            exp = base**i
            digit = (n // exp) % base
            buckets[digit].append(n)

        arr = flatten(buckets)
        buckets = [[] for _ in range(base)]

    return arr

def bucket_sort(arr: list[float], n_buckets: int | None = 10) -> list[float]:
    """
    Bucket sort only works for floats between 0 and 1
    """
    if any(n < 0 or n > 1 for n in arr):
        log_and_raise(OutOfRangeError("Bucket sort only works for floats between 0 and 1"))

    if n_buckets is None:
        n_buckets = 10


    buckets: list[list[float]] = [[] for _ in range(n_buckets)]
    for n in arr:
        index = int(n * n_buckets)
        buckets[index].append(n)

    for i, bucket in enumerate(buckets):
        buckets[i] = bubble_sort(bucket)

    return flatten(buckets)
