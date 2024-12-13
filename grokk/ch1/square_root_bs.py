# Finding the Square Root (Integer Part)
# Problem: Given a non-negative integer x, compute and return the square root of x, rounded down to the nearest integer.
# Hint: Treat the problem as finding the point where mid * mid <= x and (mid + 1) * (mid + 1) > x.

def square_root_bs(num: int):
    low = 0
    high = num
    result = 0

    while low <= high:
        middle = (low + high) // 2 # floor division must occur in b search
        if middle * middle == num: # since this cond only works for perfect squares, how can i make it adhere to my rule such that even non squares can work?
            return middle # this will be the square root
        elif middle * middle <= num: # if middle too low to be sqrt:
            result = middle
            low = middle + 1
        else:
            high = middle - 1
    return result

print(square_root_bs(25))
