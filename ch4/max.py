def my_max(nums: list):
    if len(nums) == 1:
        return nums[0]
    else:
        max_of_rest = my_max(nums[1:])
        if nums[0] > max_of_rest:
            return nums[0]
        else:
            return max_of_rest