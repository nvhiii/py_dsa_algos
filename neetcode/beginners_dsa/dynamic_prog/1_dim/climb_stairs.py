class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i, cache):
            if i >= n:
                return i == n
            if i in cache:
                return cache[i]
            
            cache[i] = dfs(i + 1, cache) + dfs(i + 2, cache) # the steps calculation
            return cache[i]

        return dfs(0, {})