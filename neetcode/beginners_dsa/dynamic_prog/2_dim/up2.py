class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # notes
        # m rows
        # n cols
        # top left to bottom right
        # only down or right
        # obstacle = 1
        # valid = 0
        # cannot iter through obs
        # find all unique paths, backtrack

        # ambiguity
        # are we guaranteed that the robot will be at 0,0 like do we know its not an obs?

        # brute force:
        # since we want to backtrack, use dfs
        # dfs = recursion
        # base case(s) check if index row / col = rows or cols or if the index has obs
        # valid case if we reached last index in matrix
        # recurse in 2 directions for each index
        # since each path limited to 2 directions, all valid paths if they exist will be n + m
        # time: 2 ^ n + m
        # space: n * m

        # approach
        # we can optimize using a dp method
        # use dfs/recursion + memoization (topdown)
        # we cache all indices, if valid or not
        # time complexit since no extra work: n * m
        # space still n * m

        # implement
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        return self.upo(obstacleGrid, 0, 0, rows, cols, [[0] * cols for i in range(rows)]) # must pass in grid as well, since we wanna see if it has obs

    def upo(self, g, r, c, rows, cols, cache):
        if r == rows or c == cols or g[r][c] == 1:
            return 0 # invalid path
        if cache[r][c] > 0: # already computed that means
            return cache[r][c]
        if r == rows - 1 and c == cols - 1:
            return 1 # valid path

        # memoize
        cache[r][c] = self.upo(g, r + 1, c, rows, cols, cache) + self.upo(g, r, c + 1, rows, cols, cache)
        return cache[r][c]