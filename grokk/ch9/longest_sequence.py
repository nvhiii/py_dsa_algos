words = ["fish", "fort"]

def longest_sequence(ustr: str):

    best_match = ""
    max_length = 0

    for word in words:
        # create matrix for each word
        # m x n , m = word n = ustr
        matrix = [[0] * (len(ustr) + 1) for _ in range(len(word) + 1)]

        current_max_length = 0

        for row in range(1, len(word) + 1): # must iterate from 1 to not run into indexing issue
            for col in range(1, len(ustr) + 1):
                if word[row - 1] == ustr[col - 1]: # check if the corresponding idx of word and ustr are same
                    matrix[row][col] = matrix[row-1][col-1] + 1
                    current_max_length = max(current_max_length, matrix[row][col]) # update
                else:
                    matrix[row][col] = max(matrix[row-1][col], matrix[row][col-1]) # find max of item above and left, and save to current idx in matrix

        if current_max_length > max_length:
            max_length = current_max_length
            best_match = word

    return f"The longest common subsequence word is {best_match}"

def main():
    ustr = input("Input a word: ")
    print(longest_sequence(ustr))

main()