def insertion_sort(arr):
    for i in range(len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]: # ensure not negative index + if prev index greater than next
            # pythonic swap
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1 # decrement in order to compare w even more prev index
    return arr
my_arr = [5, 4, 3, 1, 2]
print(insertion_sort(my_arr))