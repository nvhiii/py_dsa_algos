# imp kth smallest using one func
# keep in mind selection sort doesnt need a sorted list
def kth_smallest(nums: list, kth: int) -> int:
    for i in range(kth): # iterate until kth element, ensure get that element
        smallest_idx = i
        for j in range(i+1, len(nums)): # iterate rest of array, in order to find next smallest
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        # perform swap
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums[kth - 1] # since this arr is sorted ascending, smallest to largest, we access kth index regarding 0 idx

my_arr = [55, 44, 11, 22, 121, 132, 77, 33, 88]
print(kth_smallest(my_arr, 4)) # should return 4th smallest, expect 44