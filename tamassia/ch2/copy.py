from copy import copy, deepcopy
def copy_list(my_list: list) -> tuple:
    dc = deepcopy(my_list)
    c = copy(my_list)
    return dc, c

