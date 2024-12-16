from collections import Counter

def bs_bn(arr):
    counts = Counter(arr)
    # first sort keys
    sorted_keys = sorted(counts)

    i = 0
    for key in sorted_keys:
        for _ in range(counts):
            arr[i] = key
            i += 1

    return arr


# Test
nums = [4, 6, 4, 5]
print(bs_bn(nums))  # Output: [4, 4, 5, 6]