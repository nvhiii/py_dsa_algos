def quicksort(arr):
    return qs(arr, 0, len(arr) - 1)

def qs(arr, start, end):
    if end - start + 1 <= 1:
        return arr

    pivot = arr[end]
    left = start # this is the pointer that will go through the arr, eventually signifying
    # end of the all the vals less than the value of pivot

    for i in range(start, end):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    arr[end] = arr[left]
    arr[left] = pivot

    qs(arr, start, left - 1)
    qs(arr, left + 1, end)

    return arr

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    print(quicksort(arr))