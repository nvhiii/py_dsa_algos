def climbStairs(self, n: int) -> int:
        # n is the number, and int, decrement until smallest case, 1
        # can take steps in 1 or 2 only
        def dfs(i): # depth first search
            if i >= n: # if the current node val is greater or equal
                return i == n # if true, returns 1, adding to possible paths
            else:
                return dfs(i + 1) + dfs(i + 2)

        # initiate dfs traversal
        return dfs(0)