def unique_elements(S):
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            if j == k:
                return False
            
    return True