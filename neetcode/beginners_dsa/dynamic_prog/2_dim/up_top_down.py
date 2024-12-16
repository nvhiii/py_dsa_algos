class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # notes
        # given the dims of a matrix
        # move down and right only
        # find paths from top left to bottom right

        # ambiguity
        # what is the case to fit 32 bit? Does it mean the number cannot be insanely large?
        # also, this assumes matrix doesnt have to be square correct?
        # do you have a preference in the way i solve this problem?

        # brute force
        # since we want all paths, its likely backtracking algo
        # so prob dfs == recursion
        # base case wont care about if curr index is up or left out of bound, since we cannot move that dir
        # that returns 0^
        # base case for valid
        # if index row = m - 1 and index col = n - 1
        # recurse with a variable to store count
        # bad, bc we need to do extra work
        # this is 2 decisions to the power of moving entire row right and entire col down, m + n
        # we can do top down, starting from last index in matrix
        # have prev arr init as len n
        # then we iterate backwards for row -1
        # then we create curr row and init as len n
        # then we set last col val as 1
        # then iterate prev col vals from cols - 2
        # then update the curr index in the row as the sum of prev row col + curr row col + 1
        # then reassign pointer of prev to curr
        # exit loops and return 0th index of prev
        # time complexity: (n * m), still need to iterate all items in matrix
        # space: o(m) bc of prev arr

        # create helper
        prev = [0] * n
        for _ in range(m - 1, -1, -1):
            curr = [0] * n
            curr[n - 1] = 1
            for c in range(n - 2, -1, -1):
                curr[c] = prev[c] + curr[c + 1]
            prev = curr

        return prev[0]


        