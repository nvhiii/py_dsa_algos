def countdown(num: int):
    # id base case and recursive case
    if num <= 0:
        return
    else:
        print(num)
        countdown(num-1)

countdown(5)