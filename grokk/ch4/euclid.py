def euclid_max_squares(width: int, height: int):

    def find_dim_nums(a, b): # in this recursion, operation of splitting squares smaller is logn
        if b == 0: # base
            side = a
            num_squares = (width * height) // (side ** 2)
            return num_squares, side
        else: # recur
            return find_dim_nums(b, a % b)

    return find_dim_nums(width, height)

print(euclid_max_squares(1680, 640))