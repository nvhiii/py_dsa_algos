def merge_sort(arr, s, e):
    if e - s + 1 <= 1:
        return arr # this is the base case, where the arr length is 1

    # now we will calc middle index and split arr into smaller subprobs until base case(s)
    mid = (s + e) // 2
    merge_sort(arr, s, mid)
    merge_sort(arr, mid + 1, e)
    merge(arr, s, mid, e)

    return arr # eventually returns the whole arr, after popping all the recursive calls off the stack


# would it be more efficient to use pointers instead of creating new arrays?
def merge(arr, s , m, e):
    L = arr[s : m + 1]
    R = arr[m + 1 : e + 1]

    i = 0
    j = 0
    k = s # this pointer to the parent array to rearrange elements isnt 0, because some arrays dont start at start of the array!

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    print(merge_sort(arr, 0, len(arr) - 1))
