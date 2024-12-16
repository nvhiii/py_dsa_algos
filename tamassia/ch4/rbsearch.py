def rbinary_search(data, target, low, high):

    if low > high: # while high >= low basically base case
        return False
    else:
        mid = (low + high) // 2 # floor div in case of straggling set of odd num of nums
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return rbinary_search(data, target, low, mid - 1)
        else:
            return rbinary_search(data, target, mid + 1, high)