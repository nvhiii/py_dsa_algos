# Peak Element in a Mountain Array
# Problem: Given an array where the numbers first strictly increase, then strictly decrease, find the peak element.
# Goal: Use binary search to locate the peak where arr[mid] > arr[mid+1]

def peak_element(nums: list):
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        num_at_mid = nums[middle]
        if num_at_mid > nums[middle + 1]:
            high = middle
        else:
            low = middle + 1

    return nums[low]

my_nums = [1, 2, 3, 4, 5, 77, 99, 999]
print(peak_element(my_nums))