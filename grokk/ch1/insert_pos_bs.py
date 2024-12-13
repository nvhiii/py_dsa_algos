def insert_pos_bs(nums: list, target: int):
    # find insertion index of given num, its not in the current list
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = (low + high) // 2 # index in list calc
        num_at_mid = nums[middle]
        if num_at_mid == target:
            return middle
        elif num_at_mid < target:
            low = middle + 1
        else:
            high = middle - 1

    return low

my_nums = [1, 2, 3, 3, 4, 5]
print(insert_pos_bs(my_nums, 3)) # should be inserted at first pos
