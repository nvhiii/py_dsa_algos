# 74. Search a 2D Matrix
# Solved
# Medium
# Topics
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1 # iterating a flattened matrix
        while l <= r:
            m = l + (r - l) // 2
            rows, cols = m // COLS, m % COLS
            if target > matrix[rows][cols]:
                l = m + 1
            elif target < matrix[rows][cols]:
                r = m - 1
            else:
                return True
        return False