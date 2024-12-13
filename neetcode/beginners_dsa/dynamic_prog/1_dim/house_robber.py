class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums) # not calculated yet
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1: # computed 
                return memo[i]

            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2)) 
            # recurrence relation, in this case it 
            # skipping first index vs comparing curr 
            # index and next non adjacent
            return memo[i]

        return dfs(0)