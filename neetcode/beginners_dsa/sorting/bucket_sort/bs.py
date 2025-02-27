def bucket_sort(arr):
    # do a count

    counts = [0] * len(set(arr)) # (1, 1, 2, 3, 4, 5) = 1,2,3,4,5 = len5
    for num in arr:
        counts[num] += 1

    i = 0
    for j in range(len(counts)):
        for _ in range(counts[j]):
            arr[i] = j
            i += 1

    return arr

if __name__ == "__main__":
    arr = [4, 3, 2, 1, 0] # important is the fact that i havent figured out how to do this with arr starting at non-zero
    print(bucket_sort(arr))