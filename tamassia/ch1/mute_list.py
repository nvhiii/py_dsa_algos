def rotate_list_k(nums: list, k: int):

    # extract list from curr
    extracted_start_idx = k % len(nums) # returns index to start slicing at
    # suppose list is 5 len, we get 13 as k, start at 3. Suppose list is 5 len, k = 3, we idx at 3


    curr = nums[:-extracted_start_idx] # end exclusive
    extracted = nums[-extracted_start_idx:]
    return extracted + curr

    # when we make a negative number the start of a slice, it first finds that index by counting from the -1 index (the last element in list), then it goes to the negative number speicifed. Then, since we dont have the end of a slice value, it appends all values starting at the negative index and to its right.

nums = [1, 2, 3, 4, 5]
print(rotate_list_k(nums, 13))
