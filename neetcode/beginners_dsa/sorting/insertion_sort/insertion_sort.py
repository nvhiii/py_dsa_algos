def insertion_sort(nums: list):
    # we assume first num is organized, bc 1 element is organized
    for i in range(1, len(nums)):
        # prev number
        j = i - 1
        while j >= 0 and nums[j + 1] < nums[j]: # if next index num is greater, we iter backwards to sort and compare
            # nums[j] is the previous number, j + 1 is next num
            temp = nums[j + 1]
            nums[j + 1] = nums[j] # swapped
            nums[j] = temp
            j -= 1

    return nums # cannot be in loop, make sure to dbl check
    # stable, bc we dont swap same values
    # o(n^2)

my_nums = [5, 4, 3, 2, 1]
print(insertion_sort(my_nums))