class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = [[0,1], [0,-1], [1,0], [-1,0]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # base case
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for dr, dc in moves:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands