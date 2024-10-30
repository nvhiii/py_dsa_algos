def sum_arr(nums: list):
    if len(nums) == 0: # base, want to get nums array get smaller
        return 0
    else:
        return nums[0] + sum_arr(nums[1:]) # keeps popping first index off

my_arr = [1, 2, 3, 4, 5]
print(sum_arr(my_arr))