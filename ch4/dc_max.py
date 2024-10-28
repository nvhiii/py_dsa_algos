nums = [1, 2, 3, 4, 5]

def dc_max(nums: list):
    if len(nums) == 1:
        return nums[0]
    else:
        rest_max = dc_max(nums[1:])
        return nums[0] if nums[0] > rest_max else rest_max
    
print(dc_max(nums))