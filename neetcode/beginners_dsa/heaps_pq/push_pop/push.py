# assume we have heap initialized

def push(arr, val):
    # we dont need a check
    arr.append(val) # we append to end, now we must percolate upwards
    # keep structure, need to keep complete bst
    i = len(arr) - 1 # we we iterate from bottom node

    while i > 1 and  arr[i] < arr[i // 2]: # compare current "node" to its parent
        arr[i], arr[i // 2] = arr[i // 2], arr[i] # do swap
        i //= 2 # iter to parent if we did do swap