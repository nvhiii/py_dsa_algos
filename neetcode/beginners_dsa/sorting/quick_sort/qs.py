def quicksort(arr, s, e):
    if e - s + 1 <= 1:
        return arr
    
    # pivot and left pointers
    pivot = arr[e]
    left = s

    # iter for less
    for i in range(s, e):
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i] # swap
            left += 1

    # left has another number, need to swap w end
    arr[e] = arr[left]
    arr[left] = pivot # place pivot in right place

    # left
    quicksort(arr, s, left - 1)
    
    # right
    quicksort(arr, left + 1, e)

    return arr

nums = [5, 4, 3, 1, 2]
print(quicksort(nums, 0, len(nums) - 1))