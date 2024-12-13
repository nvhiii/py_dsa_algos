def popp(arr):

    # keep checks
    if len(arr) <= 1:
        return None
    if len(arr) == 2:
        return arr.pop()

    # store val at top since its min we want to pop
    min_val = arr[1]
    arr[1] = arr.pop() # last indexed val is new first node
    i = 1 # iterate

    while 2 * i < len(arr):
        left = 2 * i
        right = 2 * i + 1
        mv = left

        if right < len(arr) and arr[right] < arr[left]:
            mv = right

        if arr[i] < arr[mv]:
            break

        arr[i], arr[mv] = arr[mv], arr[i]
        i = mv

    return min_val