import sys

def dynamic_array_size(data: list, n):
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print(f"Length: {a} Size in bytes: {b}")
        data.append(None)


my_d_array = []
dynamic_array_size(my_d_array, 26)