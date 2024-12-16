def add_mult(my_tuple: tuple):
    product = 1
    total = 0
    for num in my_tuple:
        product *= num
        total += num

    return (total, product)

nums = (1, 2, 3, 4)
print(add_mult(nums))