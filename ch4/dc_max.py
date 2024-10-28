nums = [3, 5, 9, 3, 2]

def dc_max(nums: list):
    if len(nums) == 1:
        return nums[0]
    else:
        max_rest = dc_max(nums[1:])
        return nums[0] if nums[0] > max_rest else max_rest
    
print(dc_max(nums))