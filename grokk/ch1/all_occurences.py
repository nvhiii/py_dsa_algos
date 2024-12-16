from last_occurence import find_last_occurrence
from first_occurence import find_first_occurrence
def all_occurences(nums: list, num: int):
    first = find_first_occurrence(nums, num)
    last = find_last_occurrence(nums, num)

    if first == -1 or last == -1:
        return 0
    
    return last - first + 1

my_list = [1, 2, 3, 3, 3, 4, 5]
print(all_occurences(my_list, 3))
