def insert_end(arr, n, length, capacity):
    if length < capacity: # if num of nums less than the avail space
        arr[length] = n # we can do index of length, bc indexing starts at 0
        