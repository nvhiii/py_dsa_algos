# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

def insertionSort(pairs: list["Pair"]) -> list:
    # we have a list of pairs: k,v defined about
    # return list containing lists after each insert sort step + make a stable sort algo
    # assume 0th index sorted
    steps = [] # initializing as empty is better than printing pairs, bc what if empty?
    length = len(pairs)
    # keep in mind this covers all indices, hence it prints each step, including last sorted list of pairs
    # also, j wont be valid when i == 0, but iter will go to next index, and it will all exec
    for i in range(length): # compare from 2nd index number, w/ 0th index in mind
        j = i - 1 # this is the prev number
        while j >= 0 and pairs[j].key > pairs[j + 1].key: # j is prev index, j + 1 = i, also ensure we dont go out of bounds
            # if curr index is less than prev index, do swap
            # do a swap pythonically
            pairs[j + 1], pairs[j] = pairs[j], pairs[j + 1] # bigger index = larger val, smaller index = less val
            j -= 1
        steps.append(pairs[:]) # between each swap, we append whole list
    return steps

my_pairs = [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")]

steps = insertionSort(my_pairs)
for step in steps:
    print(step)