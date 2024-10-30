# helper
def smallest(nums: list):
    sm = nums[0]
    sm_idx = 0
    for i in range(1, len(nums)):
        if nums[i] < sm:
            sm = nums[i]
            sm_idx = i
    return sm_idx

def kth_smallest(nums: list, kth: int):
    new_arr = []
    for i in range(kth): # only up to kth smallest iterated to, inclusive loop
        index = smallest(nums)
        new_arr.append(nums.pop(index))
    return new_arr[-1] # returns after sorting up until kth smallest

my_arr = [1, 3, 5, 7, 4, 2, 8, 11, 854, 33]
print(kth_smallest(my_arr, 6))