def remove_element(arr, val):
    curr_idx = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[curr_idx] = arr[i]
            curr_idx += 1

    return curr_idx, arr