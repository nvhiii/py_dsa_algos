def insertion_sort(S):
    # 1st element assumed sorted
    for k in range(1, len(S)):
        # curr value
        curr = S[k]
        j = k
        while j > 0 and S[j - 1] > curr: # if prev index num greater than current index, do swap
            S[j] = S[j - 1]
            j -= 1
        S[j] = curr
    return S

my_arr = [4, 2, 1, 3, 5]
print(insertion_sort(my_arr))