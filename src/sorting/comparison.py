# bubble, quick, heap

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


def quick_sort(arr: list[int]) -> list[int]:
    
    def _partition(left:int, right:int) -> int:
        """Makes a partition and returns index of middle element"""
        l = left
        pivot = right - 1
        r = pivot - 1

        while l < r:
            if arr[l] >= arr[pivot] and arr[r] < arr[pivot]:
                _swap(arr, l, r)
            
            if arr[l] < arr[pivot]:
                l += 1
            
            if arr[r] >= arr[pivot]:
                r -= 1
        
        _swap(arr, l, pivot)
        pivot = l

        return pivot
    
    def _sort(left:int, right:int):
        if left - right <= 1: return
        
        pivot = _partition(left, right)
        
        _sort(left, pivot)
        _sort(pivot+1, right)

    _sort(0, len(arr)-1)
    return arr