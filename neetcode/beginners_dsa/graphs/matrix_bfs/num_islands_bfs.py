# BFS solution

from collections import deque

def numIslands(grid):
    ROWS, COLS = len(grid), len(grid[0])
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    q = deque()
    visited = set()
    islands = 0

    def bfs(r, c):
        q.append((r, c))
        visited.add((r, c))

        while q:
            for dr, dc in directions:
                # base case
                nr, nc = r + dr, c + dc
                if min(nr, nc) <= 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited or grid[nr][nc] == "0":
                    continue
                q.append((nr, nc))
                visited.add((nr, nc))

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r, c)
                islands += 1

    return islands



