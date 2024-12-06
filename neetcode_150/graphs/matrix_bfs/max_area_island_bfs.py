# from collections import deque

# def maxAreaIsland(grid):
#     ROWS, COLS = len(grid), len(grid[0])
#     visited = set()
#     q = deque()
        
#     def bfs(r, c):
#         q.append((r, c))
#         visited.add((r, c))
#         area = 0
#         while q:
#             r, c = q.popleft()
#             if min(r, c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == 0:
#                 continue
#             q.append((r,c))
#             visited.add((r,c))
#             area += 1

#         return area
    
#     area = 0
#     for r in range(ROWS):
#         for c in range(COLS):
#             area = max(area, bfs(r, c))

#     return area