def mergeSort(arr, start, end):
    # base case
    if end - start + 1 <= 1: # meaning if length 1
        return arr
    
    # split into 2 halves
    mid_idx = (start + end) // 2 # find half index
    mergeSort(arr, start, mid_idx)
    mergeSort(arr, mid_idx + 1, end)

    # recur call to merge
    merge(arr, start, mid_idx, end)

    return arr
    
def merge(arr, s, m, e):
    L = arr[s : m + 1]
    R = arr[m + 1 : e + 1]

    i = 0 # pointer to L
    j = 0 # pointer to R
    k = s # pointer to arr

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1 # iterate pointer to next index in L
        else:
            arr[k] = R[j]
            j += 1 # iterate pointer to next index in R
        # in either case, k is iterated
        k += 1

    # for if L or R is longer in length
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

arr = [4, 5, 3, 2, 1]
print(mergeSort(arr, 0, len(arr) - 1))

