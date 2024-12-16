# Unique Elements in a List
# Write a function that takes a list of integers and returns a list of unique elements in the order they first appear, without using a loop or list comprehension for duplicates. For example, [1, 2, 2, 3, 4, 4, 5] should return [1, 2, 3, 4, 5].

def order_set(nums: list):
    seen = set()
    return [num for num in nums if not (num in seen or seen.add(num))] # short circuit eval, only evals first part unless false
