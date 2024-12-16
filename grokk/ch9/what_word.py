words = [
    "fish", "vista"
]

def what_word(ustr: str):
    # word = words[0] # fish
    # create matrix of m (len of fish word) by n (len of ustr)
    # matrix = [[0] * (len(ustr)+1) for _ in range(len(word)+1)]

    best_match = ""
    max_length = 0

    for word in words:
        matrix = [[0] * (len(ustr) + 1) for _ in range(len(word) + 1)]

        current_max_length = 0

        for row in range(1, len(word) + 1): # since we iterate from 1 to avoid errors such as no val error
            for col in range(1, len(ustr) + 1):
                if word[row - 1] == ustr[col - 1]: # we access prev, check if character at intersection is equal
                    matrix[row][col] = matrix[row-1][col-1] + 1 # find upper left diagonal item and add 1 to it
                    current_max_length = max(current_max_length, matrix[row][col])
                else:
                    matrix[row][col] = 0

        if current_max_length > max_length:
            max_length = current_max_length
            best_match = word

    return f"The closest match is {best_match}"

def main():
    u_input = input("Enter a string: ")
    print(what_word(u_input))

main()
