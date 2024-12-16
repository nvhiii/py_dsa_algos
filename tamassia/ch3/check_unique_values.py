def c_unique_values(A, B, C):
    for num in A:
        for num2 in B:
            if num == num2: # this if ensures C only executes n times
                for num3 in C:
                    if num == num3:
                        return False
    return True

    # A and B nested loops are n^2 time