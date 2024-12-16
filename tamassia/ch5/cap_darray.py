import sys
# getsizeof
def new_capacity(data, n):
    prev_size = sys.getsizeof(data)
    for k in range(n):
        curr_size = sys.getsizeof(data)
        # implement a check for every 5 indexes, from 0
        if curr_size > prev_size or len(data) == 0:
            length = len(data)
            space_needed = sys.getsizeof(data)
            print(f"Length of list: {length}, Space in bytes: {space_needed}")
            prev_size = curr_size

        data.append(None)

my_d_array = []
new_capacity(my_d_array, 26)