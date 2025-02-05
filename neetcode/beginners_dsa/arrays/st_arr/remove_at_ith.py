def remove_at_ith(arr, i):
    for index in range(i + 1, len(arr)):
        arr[index - 1] = arr[index]

if __name__ == "__main__":
    new_arr = [3, 4, 5, 2, 1]
    remove_at_ith(new_arr, 0)
    print(new_arr)