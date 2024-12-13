"""Q: Find the length of the shortest path from the top left of the grid to the bottom right"""

from collections import deque

def matrix_bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()
    visited = set() # hashset to track visited nodes
    # add first point, top left of 0,0
    q.append((0,0))
    visited.add((0,0))

    length = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length
            
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for dr, dc in directions:
                if min(r + dr, c + dc) < 0 or r + dr >= ROWS or c + dc >= COLS or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == 1:
                    continue
                q.append((r + dr, c + dc))
                visited.add((r + dr, c + dc))

        length += 1

    return length