def prefix_average_2(S):
    A = [0] * len(S)
    for j in range(len(S)):
        A[j] = sum((S[:j+1])) / (j + 1)
    return A

# still n^2 because the slicing operation instantiates new list, not really efficient