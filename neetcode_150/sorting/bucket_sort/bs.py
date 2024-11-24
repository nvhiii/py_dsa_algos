def bucket_sort(arr):
    counts = [0] * len(set(arr))
    for num in arr:
        counts[num] += 1

    # if larger numbers, better to use hashmap, this is a very simple example
    # or use a tuple, usually hm better

    i = 0 # iterate in the counts
    for n in range(len(counts)):
        for _ in range(counts[n]): # this iterates n times for 1 iteration of outer loop
            arr[i] = n
            i += 1

    return arr

my_nums = [0, 1, 2, 2, 2, 1, 0, 2, 1]
print(bucket_sort(my_nums))