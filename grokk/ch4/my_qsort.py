# suick sort is unsorted, similar to selection sort, but nlogn
def my_qsort(nums: list):
    pivot = nums[0]
    less = [num for num in nums if num <= pivot]
    more = [num for num in nums if num > pivot]
    if len(nums) < 2:
        return nums
    else:
        my_qsort(less) + [pivot] + my_qsort(more)

my_arr = [5, 6, 7, 1, 2, 3, 9]
print(my_qsort(my_arr))