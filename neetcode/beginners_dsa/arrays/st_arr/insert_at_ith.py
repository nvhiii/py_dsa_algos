def insert_at_ith(arr, i, element, length):
    for index in range(length - 2, i - 1, -1):
        # cannot do length - 1 as start fro some reason? why? bc we wanted extra space lol

        # why i - 1 for stop? because we dont want to shift the elements before the index i
        arr[index + 1] = arr[index] # next index val is the previous index val
        # inherently shifting everything to the right

    arr[i] = element


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 0]
    insert_at_ith(arr, 2, 3, len(arr))
    print(arr)