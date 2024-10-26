def binary_search(my_list: list, item: int):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = my_list[middle]
        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        if guess < item:
            low = middle + 1
    return None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(binary_search(my_list, 3))