def uniqueness_2(S):
    new = sorted(S) # quicksort is nlogn time
    for j in range(1, len(S)): # n time, 1 loop
        # we start at 1 to compare curr and prev index
        if S[j-1] == S[j]:
            return False
        
    return True