def recur_summation(S, index=0):
    """Summation of a series, S, using recursion"""
    if index == len(S):
        return 0
    else:
        return S[index] + recur_summation(S, index + 1) # sum curr idx and list starting at next index
    
my_nums = [1, 2, 3, 4, 5]
print(recur_summation(my_nums))