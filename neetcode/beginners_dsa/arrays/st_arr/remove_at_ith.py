def remove_at_ith(arr, i, length):
    """params: static arr, index to remove, length of arr"""
    for index in range(i + 1, length): # we iterate using index instead of i since we dont want to change i vals
        arr[index - 1] = arr[index] # shift nums on right by 1 unit to left each
        # basically, index = i + 1, hence index - 1 = i