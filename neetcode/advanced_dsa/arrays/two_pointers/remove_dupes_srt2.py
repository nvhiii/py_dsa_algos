class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # givne
        # nums in non decreasing order, meaningthere could be dupes
        # remove in place so arr has any num a MAX of 2 times
        # keep relative order

        # intuition
        # track the index for insertion, will be init at 0
        # create a var for window size, 2 (max num for each unique element!)
        # iterate all nums
        # for num in nums
        # have if cond
        # check if index < k OR nums[index - k] != num, so we can make sure we dont get index - k out of bound serrors + check for dupes outside the range of 2
        # then the nums curr index = num
        # then inc index

        # return curr index after all iter
        # time: o(n), one pass solution
        # space: o(1) no extra mem allocated

        win_size = 2
        curr_idx = 0
        for num in nums:
            if curr_idx < win_size or nums[curr_idx - win_size] != num:
                nums[curr_idx] = num
                curr_idx += 1

        return curr_idx # this is the size of the arr after we fit the constraint every num cannot be shown more than twice!