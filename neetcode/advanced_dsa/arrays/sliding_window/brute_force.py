# Given an array, return true if there are two elements within a window of size k that are equal.
def sliding_window(arr, k):
    # the brute force implementation
    # iterate the arr
    for L in range(len(arr)):
        # we iterate the arr of n size
        for R in range(L + 1, min(len(arr), L + k)): # finding the min ensures the window never goes out of bounds
            # for each index, we iterate until the window size reached, m
            if arr[L] == arr[R]:
                return True
            
        # therefore, time complexity is O(n * m)
        # also, space complexity is simply O(1), no extra data structure created
    
    return False # even after iteration, found nothing so false