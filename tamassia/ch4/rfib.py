def recursive_fibonacci(n):
    if n <= 1:
        return 1
    else:
        # tuple to store a, b
        (a, b) = recursive_fibonacci(n - 1) # prev num is a + b, b is a
        return (a + b, a) 