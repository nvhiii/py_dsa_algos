def count_swaps(nums: list):
    swaps = 0
    # we need to sort in ascending order
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        # perform each swap
        if smallest_idx != i: # check if the swap going through
            nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
            swaps += 1

    return swaps

my_arr = [55, 44, 11, 22, 121, 132, 77, 33, 88]
print(f"The number of swaps required to sort {my_arr} is {count_swaps(my_arr)}")