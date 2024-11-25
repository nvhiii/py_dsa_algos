# in this example, we dont actually have a target to look for, we have an algorithm
# to check if its the value we seek

def binary_search(low, high):
    while low <= high:
        mi = low + (high - low) // 2
        # no target so no guess
        if isCorrect(mi) > 0: # too large
            high = mi - 1
        elif isCorrect(mi) < 0: # too small
            low = mi + 1
        else:
            return mi



def isCorrect(num):
    if num > 10:
        return 1
    elif num < 10:
        return -1
    else:
        return 0