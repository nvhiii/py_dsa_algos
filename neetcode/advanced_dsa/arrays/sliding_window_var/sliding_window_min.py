class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # given
        # nums arr
        # target val
        # find min len subarr where its sum >= target
        # else return 0, meaning no subarr sums to target

        # brute force / intuition
        # since we need to compare the sums
        # track sum
        # track len
        # track L + R pointers, will make sense bc we want to find subarr and length can be calc R - L + 1
        # each iter, we add nums[R] to the currSum
        # while currSum >= target
        # we remove L index val
        # substract that L index from currSum
        # update len = min(currlen, R - L + 1) inside loop
        # return 0

        currSum, length = 0, float("inf")
        L = 0
        for R in range(len(nums)):
            currSum += nums[R]
            while currSum >= target:
                length = min(length, R - L + 1) # must be first before L is altered to do comparison
                currSum -= nums[L]
                L += 1 # move L to the right

        return 0 if length == float("inf") else length

        # time: O(n)
        # space: O(1)