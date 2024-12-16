def insert_at_ith(arr, i, n, length):
    for index in range(length - 1, i, -1): # we first want to create a gap, hence we iterate from end of sequence to create gap
        arr[index + 1] = arr[index]

    arr[i] = n