def delete_end(arr, length): # soft delete of element at last index
    """params: static arr, static array num of elements"""
    if length > 0: # ensure arr length is valid
        arr[length - 1] = 0 # this is a soft delete, o(1) time delete since at end