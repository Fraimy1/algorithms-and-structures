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

        if had_swaps == False:
            break

    return arr

def get_min_max(arr: list[int]) -> tuple[int, int]: 
    cur_min, cur_max = 0, 0

    for n in arr:
        if n < cur_min:
            cur_min = n
        
        if n > cur_max:
            cur_max = n
    return cur_min, cur_max

def counting_sort(arr: list) -> list[int]:
    
    min_n, max_n = get_min_max(arr)
    
    shift = 0
    if min_n < 0:
        shift = abs(min_n)

    min_n, max_n = min_n + shift, max_n + shift

    counts = [0 for _ in range(min_n, max_n+1)]
    for n in arr:
        counts[n+shift] +=1
    
    return [value-shift for value, count in enumerate(counts, start=min_n) for _ in range(count)]