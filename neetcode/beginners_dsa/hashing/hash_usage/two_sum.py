class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        val_to_index = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in val_to_index:
                return [val_to_index[diff], i]
            else:
                val_to_index[nums[i]] = i