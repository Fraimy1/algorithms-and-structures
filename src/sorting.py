from src.core.errors import NegativeNumberError
from src.core.errors import OutOfRangeError

def bubble_sort(arr: list[int]) -> list[int]:
    had_swaps = False

    while True:
        had_swaps = False

        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                tmp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = tmp
                had_swaps = True

        if not had_swaps:
            break

    return arr

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
        raise NegativeNumberError("Radix sort only works for positive numbers") 

    if not arr:
        return arr
    
    if len(arr) ==1:
        return arr

    buckets = [[] for _ in range(base)]
    
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
        raise OutOfRangeError("Bucket sort only works for floats between 0 and 1")

    if n_buckets is None:
        n_buckets = 10


    buckets = [[] for _ in range(n_buckets)]
    for n in arr:
        index = int(n * n_buckets)
        buckets[index].append(n)

    for i, bucket in enumerate(buckets):
        buckets[i] = bubble_sort(bucket)
    
    return flatten(buckets)

def _swap(arr: list, a:int, b:int) -> None:
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def heapify(arr:list[int], parent:int, limit:int) -> None:
    while True:
        left = 2*parent + 1
        right = 2*parent + 2

        largest = parent
        
        if left < limit and arr[left] > arr[largest]:
            largest = left
            
        if right < limit and arr[right] > arr[largest]:
            largest = right

        if largest == parent:
            break

        _swap(arr, parent, largest)
        parent = largest


def heap_sort(arr: list[int]) -> list[int]:

    #Heapify - phase 1
    last_non_leaf = len(arr) // 2 - 1
    for i in range(last_non_leaf, -1, -1):
        heapify(arr, i, len(arr))
    
    #Sort down - phase 2
    end = len(arr) - 1
    while end > 0:
        _swap(arr, 0, end)
        
        heapify(arr, 0, end)
        
        end -= 1
    
    return arr