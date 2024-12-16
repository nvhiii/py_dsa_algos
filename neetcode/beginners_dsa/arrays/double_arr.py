def getConcatenation(nums):
    if nums: # valid nums list
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums