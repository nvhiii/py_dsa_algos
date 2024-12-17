def sliding_window_o(arr, k):
    # analyze the problem
    # try not to allocate new data struct
    window = set() # O(n) space?
    L = 0

    for R in range(len(arr)):
        if R - L + 1 > k: # out of bounds window size
            # first we remove the L index arr item
            window.remove(arr[L])
            # move the pointer L to the right
            L += 1
        # check if we have a dupe in the window, then true
        if arr[R] in window:
            return True
        
        # keep adding to the window until whole arr done
        window.add(arr[R])

    # if iteration done, we dont find our stuff
    return False

    # therefore time complexity is iterating the whole arr once, but continuously updating the window and its pointers, hence O(n)
    # space complexity is O(k) due to the hashset, where size of the window is size k