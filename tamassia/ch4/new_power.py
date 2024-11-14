def new_power(x, n):
    if n == 0:
        return 1
    else:
        partial = new_power(x, n // 2) # split power by 2 to get rid of unwanted odds, this is the O(logn) step since we halved operations needed to be done
        result = partial * partial # this result is the same base to the half power multiplied by itself
        if n % 2 == 1: # check if power is odd
            result *= x # accounts for floor divided odd powers
        return result