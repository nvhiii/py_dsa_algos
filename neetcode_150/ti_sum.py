def ti_sum(nums: list, target: int) -> list:
    mapped = {} # num -> idx
    for i, num in enumerate(nums):
        diff = target - num
        if diff in mapped:
            return [mapped[diff], i]
        mapped[num] = i

nums = [3,4,5,6]
target = 7
print(ti_sum(nums, target))