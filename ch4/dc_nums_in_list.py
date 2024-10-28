def nums_in_list(nums: list):
    if not nums:
        return 0
    else:
        return 1 + nums_in_list(nums[1:])
    
nums = [1, 2, 3]
print(nums_in_list(nums))