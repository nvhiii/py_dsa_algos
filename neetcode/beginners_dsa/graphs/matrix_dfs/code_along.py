# count the unique paths from the top left to the bottom right. A single path may only move along 0;s and can't visit the same cell more than once.

# my matrix dfs understanding

matrix = [[0,0,0,0],
          [1,1,0,0],
          [0,0,0,1],
          [0,1,0,0]]

def matrix_dfs(grid, r, c, visited): # grid is matrix, r c are indices, visited is a hashset
    ROWS, COLS = len(grid), len(grid[0])
    # base case(s)
    if min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == 1:
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1
    
    visited.add((r, c)) # remember to add index to visited before updating counts

    count = 0 # initialize
    # 4 directions to move
    count += matrix_dfs(grid, r + 1, c, visited) # down
    count += matrix_dfs(grid, r - 1, c, visited) # up
    count += matrix_dfs(grid, r, c + 1, visited) # right
    count += matrix_dfs(grid, r, c - 1, visited) # left

    # backtrack the path        
    visited.remove((r, c))
    return count # count is updated appropriately via backtracking
    
print(matrix_dfs(matrix, 0, 0, set()))