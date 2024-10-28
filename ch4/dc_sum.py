def dc_sums(nums: list):
    if not nums:
        return 0
    else:
        return nums[0] + dc_sums(nums[1:])
        
my_nums = [1, 2, 3, 4, 5] # sum of 15
print(dc_sums(my_nums))