def remove_dupes(arr):
    # check if arr exists
    if not arr:
        return 0

    curr_idx = 1
    for i in range(1, len(arr)): # start at 1, since we want to compare
        if arr[i] != arr[i - 1]: # compare contiguous elements
            arr[curr_idx] = arr[i] # since curr idx = 1, we assume 0th index is alr sorted
            curr_idx += 1

    return curr_idx