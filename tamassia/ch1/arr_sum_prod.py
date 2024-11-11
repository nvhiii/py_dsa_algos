from array import array
from math import prod

def arr_sum_prod(arr: array):
    total = sum([num for num in arr])
    product = prod([num for num in arr])
    return total, product

my_arr = array('i', [1, 2, 3, 4])
print(arr_sum_prod(my_arr))