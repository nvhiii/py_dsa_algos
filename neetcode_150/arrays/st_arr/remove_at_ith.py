def remove_at_ith(nums, del_idx, length):

    for i in range(del_idx + 1, length):
        nums[i - 1] = nums[i]