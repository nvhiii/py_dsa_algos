# define lambda fxn helper criterion
def find_greatest(nums: list):
    biggest = nums[0]
    bg_idx = 0
    for i in range(1, len(nums)):
        if nums[i] > biggest:
            biggest = nums[i]
            bg_idx = i
    
    return bg_idx

def sort_desc(nums: list):
    new_arr = []
    for i in range(len(nums)):
        biggest = find_greatest(nums)
        new_arr.append(nums.pop(biggest))

    return new_arr

my_arr = [3, 4, 1, 2, 5]
print(sort_desc(my_arr))