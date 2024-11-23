def quick_sort(arr, s, e):
    # base
    if e - s + 1 <= 1:
        return arr
    
    # pivot and left pointer
    pivot = arr[-1]
    left = s # first start iter from beginning of list

    # iter for finding less than pivot
    for i in range(s, e):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left] # left swaps w curr val compared if curr val less
            left += 1

    # now insert pivot
    arr[e] = arr[left] # end is given val at left pivot
    arr[left] = pivot

    # recur calls
    quick_sort(arr, s, left - 1) # left is pivot
    quick_sort(arr, left + 1, e)

    return arr

nums = [5, 4, 3, 1, 2]
print(quick_sort(nums, 0, len(nums) - 1))
