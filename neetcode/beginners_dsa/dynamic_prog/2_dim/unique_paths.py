# this solution is a top down solution using memoization + caching

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dimensions of grid are m x n (rows and cols indexed from 1)
        # can move down or right
        # find all paths from top left to bottom right

        # ambiguity:
        # what does mean fit in a 32 bit int mean?
        # A: idk
        # run through, down right per iter of index in arr

        # brute force:
        # since we know its a collection of all paths given constraints, we use backtracking
        # good approach is often dfs, using recursion
        # however, since each index has 2 options to move and each path has to iterate entire row or col eventually
        # it will be 2 ^ (m + n)
        # we can use memoization to cache, top down approach

        # approach
        # call helper first for appropriate approach, since m by n are the rows and cols
        return self.up(0, 0, m, n, [[0] * n for i in range(m)]) # n is the cols, m is rows

    def up(self, r, c, m, n, cache):
        # base case for out of bounds, no need to care about negatives
        if r == m or c == n:
            return 0 # invalid path
        if cache[r][c] > 0: # check if visited, will have a value of path from that index in matrix
            return cache[r][c]
        # valid path case
        if r == m - 1 and c == n - 1:
            return 1

        # add to cache
        # we have 2 paths, so 2 recursive calls for row below and col to right to calc index value for paths
        cache[r][c] = self.up(r + 1, c, m, n, cache) + self.up(r, c + 1, m, n, cache)
        return cache[r][c]