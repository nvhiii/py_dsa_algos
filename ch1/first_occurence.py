def find_first_occurrence(nums, target):
    low, high = 0, len(nums) - 1
    first_index = -1  # Default value if target not found

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first_index = mid  # Possible first occurrence found
            high = mid - 1     # Continue searching to the left
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first_index