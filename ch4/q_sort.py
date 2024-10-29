# O(nlogn) solution, n items in list * logn layers
def q_sort(nums: list):
    # dc
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if i <= pivot]
        more = [i for i in nums[1:] if i > pivot]
        return q_sort(less) + [pivot] + q_sort(more)
    
nums = [1, 2, 4, 6, 7, 4, 4213, 4, -1, 3]
print(q_sort(nums))