def prefix_average_3(S: list):
    running_total = 0
    length = len(S)
    A = [0] * length # creating this is O(n) time
    for j in range(length): # this is also O(n) time
        running_total += S[j]
        A[j] = (running_total) / (j + 1)
    return A

    # everything else is constant time O(1), hence efficiency is O(n), linear