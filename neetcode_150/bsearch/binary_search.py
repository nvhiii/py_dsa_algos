# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in 
# O
# (
# l
# o
# g
# n
# )
# O(logn) time.

def search(nums: list, target: int) -> int:
    low = 0
    high = len(nums)
    while low <= high:
        middle = (low + high) // 2 # gives lower of middle if not middle
        middle_num = nums[middle]
        if target == middle_num:
            return middle
        elif middle_num < target:
            low = middle + 1
        else:
            high = middle - 1
    
    return -1

nums = [-1,0,2,4,6,8]
target = 4

print(search(nums, target))