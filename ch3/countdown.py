# ez recur prac
def countdown(num: int):
    print(num)
    if num <= 0:
        return
    else:
        countdown(num-1)

countdown(5)