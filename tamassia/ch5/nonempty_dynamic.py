import sys

def ned(nums, n):
    prev = sys.getsizeof(nums)
    for k in range(n):
        curr = sys.getsizeof(nums)
        if curr > prev or len(nums) == 0:
            length = len(nums)
            sr = curr
            print(f"length: {length}, space: {sr}")
            prev = curr
        my_nums.append(k)

my_nums = [1, 2, 3]
ned(my_nums, 10)