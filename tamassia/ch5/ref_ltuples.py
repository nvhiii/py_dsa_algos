from copy import deepcopy

my_list = [1, 2, 3, 4, 5]
shallow = my_list.copy() # shallow copy 
deep = deepcopy(my_list)

my_list.extend([1, 2, 3, 4, 5])
print(my_list)

