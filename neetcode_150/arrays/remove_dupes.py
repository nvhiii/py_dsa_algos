def removeDuplicates(nums):
    # since we need to compare contiguous elements in list, need to start iter at 1
    # first check if list empty
    if not nums:
        return 0
    
    curr_idx = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]: # we assume idx 1 is diff, hence we start adding at idx 1
            nums[curr_idx] = nums[i] # basically we reordering the list through reassignment via idx not creating new ds
            curr_idx += 1

    return curr_idx
