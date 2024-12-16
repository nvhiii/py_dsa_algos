def recursive_factorial(num: int):
    if num == 0: # base case
        return 1
    else:
        return num * recursive_factorial(num-1)
    
print(recursive_factorial(5))