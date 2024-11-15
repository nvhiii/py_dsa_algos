# reversefile.py
from arraystack import ArrayStack  # Import ArrayStack

def r_file(filename):
    stack = ArrayStack()
    try:
        with open(filename, "r") as infile:
            for line in infile:
                stack.push(line.strip())
    except FileNotFoundError:
        print(f"File {filename} not found")
        return  # Stop execution if file not found

    with open(filename, "w") as outfile:
        while not stack.is_empty():
            outfile.write(stack.pop() + "\n")

# Call the function to test
r_file("pets.txt")
