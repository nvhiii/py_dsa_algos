def prefix_average1(S):
    n = len(S)
    A = [0] * n

    # nested for loops of n^2 time
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = total / (j + 1)

    return A

# returns a list of averages for nested lists up until the index specified in the given list