def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1

    return arr

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    print(insertion_sort(arr))