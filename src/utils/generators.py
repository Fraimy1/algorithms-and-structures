import random
from src.utils.validators import GeneratorValidator

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    if GeneratorValidator.check_rand_int_array(n, lo, hi, distinct=distinct) == []:
        return []

    rng = random.Random(seed)

    if distinct:
        return rng.sample(range(lo, hi+1), n)

    return [rng.randint(lo, hi) for _ in range(n)]


def _swap(arr: list, a:int, b:int) -> None:
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def nearly_sorted(n: int, swaps: int, *, seed=None) ->list[int]:
    if GeneratorValidator.check_nearly_sorted(n, swaps) == []:
        return []

    rng = random.Random(seed)

    arr = list(range(n))

    for _ in range(swaps):
        a, b = rng.sample(range(n), 2)
        _swap(arr, a, b)

    return arr


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    if GeneratorValidator.check_many_duplicates(n, k_unique) == []:
        return []

    rng = random.Random(seed)

    batch_len = n // k_unique
    last_batch = n % k_unique
    arr = []

    for i in range(k_unique):
        current_batch_len = batch_len + (1 if i < last_batch else 0)
        value = i
        arr.extend([value] * current_batch_len)

    rng.shuffle(arr)
    return arr

def reverse_sorted(n: int) -> list[int]:
    if GeneratorValidator.check_reverse_sorted(n) == []:
        return []

    return list(range(n, 0, -1))


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    if GeneratorValidator.check_rand_float_array(n, lo, hi) == []:
        return []

    rng = random.Random(seed)

    return [rng.uniform(lo, hi) for _ in range(n)]
