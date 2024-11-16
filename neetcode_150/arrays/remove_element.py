def removeElement(nums, val):
    # in a removal, try not to create new ds
    # we dont need to compare contiguous elements, so can iterate from start of list
    curr_idx = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[curr_idx] = nums[i]
            curr_idx += 1

    return curr_idx