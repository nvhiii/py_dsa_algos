def hanoi(a: list, b: list, c: list, num_disks: int):
    """move all items from a to c, top must be least, hence order descending, a already sorted"""
    if num_disks == 1:
        c.append(a.pop())
    else:
        # a -> b w/ c as proxy
        hanoi(a, c, b, num_disks-1)

        # a -> c w/ b as proxy
        c.append(a.pop())

        # b - > w/ a as proxy
        hanoi(b, a, c, num_disks-1)