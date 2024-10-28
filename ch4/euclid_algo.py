def find_largest_squares(width: int, height: int):
    
    # helper
    def gcd_recur(a, b): # a is larger, b is smaller
        if b == 0: # base case
            side = a
            num_squares = (width * height) // (side * side)
            return num_squares, side # gcd is the side returned
        else:
            return gcd_recur(b, a % b)
        
    return gcd_recur(width, height)

print(find_largest_squares(1680, 640))