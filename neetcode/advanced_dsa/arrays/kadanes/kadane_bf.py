# solution for finding max sum of a subarr in a given arr
# subarr is defined by any num of contiguous elemtns within given arr

def maxSubarr(arr):
    maxSum = arr[0]
    
    for i in range(len(arr)): # iterate the entire arr
        currSum = 0
        for j in range(i, len(arr)): # iterate starting from index i, so we dont check prev indices, only move right
            currSum += arr[j]
            maxSum = max(maxSum, currSum)

    return maxSum

n = [1, 3, -1, 2, 5, 3, -10, 1, 2, 6]
print(maxSubarr(n))


