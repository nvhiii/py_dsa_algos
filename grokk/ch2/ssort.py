def ssort(arr: list): # unordered assumed
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

my_arr = [2, 1, 3, 5, 4]
print(ssort(my_arr))