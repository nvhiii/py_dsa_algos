class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top down approach
        # move down or move right
        # m rows
        # n cols
        # find all paths, backtracking from top left to top right

        # questions: what is the need of a 32 bit int answer?
        # idk

        # brute force:
        # backtrack using dfs -> recursion (a lot of extra work)
        # t: recursion tree = 2 branches per decision, n + m movement, 2 ways so 2 ^ n + m
        # s: n * m since matrix

        # approach
        # bu 2dp, tabulation
        # since we know the base case is a valid path, why not start from there
        # since valid movements are restricted to down and right, we know bottom row and last col all 1s
        # we need the prev row and curr row to calculate all vals in curr row
        # we iterate by row then make last val in each row a 1, then iterate the col and populate it
        # then we reassing ref
        # then we retrun 0th index of prev pointer
        # time = n * m, no extra work
        # space: 2 * m = m

        prev = [0] * n # n is cols
        
        for _ in range(m - 1, -1, -1):
            curr = [0] * n # n cols
            curr[n - 1] = 1 # last val of each row is 1
            # iterate entire row vals, populate (we start at n - 2 bc we already know n - 1)
            for c in range(n - 2, -1, -1):
                curr[c] = prev[c] + curr[c + 1]
            prev = curr
        return prev[0]