def del_end(nums, length):
    """
    making last num 0"""
    if length > 0:
        nums[length - 1] = 0

    # not using len(nums) and nums[-1] bc i want to try on compact array not dynamic
