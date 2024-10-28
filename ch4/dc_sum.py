def dc_sums(nums: list):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + dc_sums(nums[1:])

my_nums = [1, 2, 3, 4, 5]
print(dc_sums(my_nums))