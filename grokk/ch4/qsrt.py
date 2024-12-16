from random import randint

def qsrt(arr: list):
    if len(arr) < 2:
        return arr
    else:
        pivot_index = randint(0, len(arr)-1)
        pivot = arr[pivot_index]
        less = [num for i, num in enumerate(arr) if i != pivot_index and num <= pivot]
        more = [num for i, num in enumerate(arr) if i != pivot_index and num > pivot]
        return qsrt(less) + [pivot] + qsrt(more)
    
my_arr = [5, 4, 3, 1, 2, 5, 6, 7, 11, 423]
print(qsrt(my_arr))
