def factorial(num: int):
    if num < 0:
        print("Erroneous input")
        return -1
    elif num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(-1))