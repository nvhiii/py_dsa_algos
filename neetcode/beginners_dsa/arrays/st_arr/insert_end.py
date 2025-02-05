def insert_end(arr, length, capacity, element):
    # in static arr, u must ensure that length/size isnt greater than capacity, or will get error
    if length < capacity:
        arr[length] = element

    # length = number of elements, think of it as size
    # capacity = max amt to hold for this arry