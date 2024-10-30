# in order to get best run time, always have random pivot
import random
def quicksort(nums: list):
    if len(nums) < 2:
        return nums
    else:
        # pivot is a single number, hence its already "sorted"
        index = random.randint(0, len(nums) - 1)
        pivot = nums[index]
        # make sure not to include pivot in these arrays
        less = [num for i, num in enumerate(nums) if num <= pivot and i != index]
        more = [num for i, num in enumerate(nums) if num > pivot and i != index]
        return quicksort(less) + [pivot] + quicksort(more)
        # basically creates huge call stack of pivots, then pops in end to sort

my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quicksort(my_arr))