class Solution:
    def dupe_int(nums: list) -> bool:
        return len(set(nums)) != len(nums)
    
    my_nums = [1, 2, 3, 4]
    print(dupe_int(my_nums))