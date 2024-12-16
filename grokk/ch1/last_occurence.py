def find_last_occurrence(nums, target):
    low, high = 0, len(nums) - 1
    last_index = -1  # Default value if target not found

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            last_index = mid  # Possible last occurrence found
            low = mid + 1     # Continue searching to the right
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last_index

# my_nums = [4, 3, 4, 2, 1, 2, 4]
# print(last_occurence(my_nums, 4))