def last_occurence(nums: list, item: int):
    low = 0
    high = len(nums) - 1
    found = -1
    while low <= high:
        middle = (low + high) // 2
        guess = nums[middle]

        if guess == item:
            found = middle
            low = middle + 1 # checking if appears again
        elif guess > item:
            high = middle - 1
        else:
            low = middle + 1

    return found if found != -1 else None

my_nums = [4, 3, 4, 2, 1, 2, 4]
print(last_occurence(my_nums, 4))