# this is an example of a fractal
# aka self recursive struct at diff scopes

# use 3 methods for implementation

def draw_line(length: int, inch_label=""):
    line = "-" * length
    if inch_label: # if label is not None
        line += " " + inch_label
    print(line)

def print_interval(center_length: int):
    if center_length > 0: # base case
        print_interval(center_length - 1)
        draw_line(center_length)
        print_interval(center_length - 1) # mirrors opposite side of each marker on ruler

def print_ruler(num_inches: int, ml: int):
    draw_line(ml, "0")
    for j in range(1, num_inches + 1):
        print_interval(ml - 1)
        draw_line(ml, str(j))
