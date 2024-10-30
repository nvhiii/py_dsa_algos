# in this sorted evens methodology, odds wont be ordered. Only evens ascending
def sort_evens(nums: list):

    # get evens
    evens_n_idx = [(even, idx) for idx, even in enumerate(nums) if even % 2 == 0]
    sorted_evens = [even for even, _ in evens_n_idx] # only get even

    # sort the evens now ascending order
    for i in range(len(sorted_evens)):
        min_idx = i
        for j in range(i + 1, len(sorted_evens)):
            if sorted_evens[j] < sorted_evens[min_idx]:
                min_idx = j

        # do swap
        sorted_evens[i], sorted_evens[min_idx] = sorted_evens[min_idx], sorted_evens[i]

    # use for loop to iterate through zipped tuples, update og list and index of even w num itself
    for (num, index), even_number in zip(evens_n_idx, sorted_evens):
        nums[index] = even_number

    return nums

# Testing
my_arr = [55, 44, 11, 22, 121, 132, 77, 33, 88]
print(sort_evens(my_arr))  # Expected output: [55, 22, 11, 44, 121, 88, 77, 33, 132]