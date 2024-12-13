def count_items(items: list):
    if len(items) == 0:
        return 0
    else:
        return 1 + count_items(items[1:])
    
my_arr = [1, "1dwd", 2, 3.45, 5]
print(count_items(my_arr))
    
        