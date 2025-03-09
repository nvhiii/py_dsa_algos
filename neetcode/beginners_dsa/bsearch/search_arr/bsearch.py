def binary_search(arr, target):
    L, R = 0, len(arr) - 1
    while L <= R: # this is to ensure that the pointers cannot cross one another
        mid = L + (R - L) // 2
        if arr[mid] < target:
            L = mid + 1
        elif arr[mid] > target:
            R = mid - 1
        else:
            return True # return the target, actually prob bool if found
    return False

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    print(binary_search(arr, target))