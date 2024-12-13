def quick_sort(arr, s, e):
    # check arr len
    if e - s + 1 <= 1:
        return arr
    
    pivot = arr[e]
    left = s # ready to iter

    # lower half
    for i in range(s, e):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left] # swap if curr is less than left element
            left += 1
    
    # shift pivot in place 
    arr[e] = arr[left] # store curr left we iter to at end
    arr[left] = pivot

    quick_sort(arr, s, left - 1)
    quick_sort(arr, left + 1, e)

    return arr

nums = [4, 5, 3, 1, 2]
print(quick_sort(nums, 0, len(nums) - 1))