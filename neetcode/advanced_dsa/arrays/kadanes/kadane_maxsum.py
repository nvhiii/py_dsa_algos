def max_sum_kadane(arr):
    maxSum = arr[0]
    currSum = 0

    # find in one pass
    for n in arr:
        currSum = max(currSum, 0) # ensure not negative, then we restart calc if so
        currSum += n
        maxSum = max(maxSum, currSum)

    return maxSum

n = [1, 3, -1, 2, 5, 3, -10, 1, 2, 6]
print(max_sum_kadane(n))