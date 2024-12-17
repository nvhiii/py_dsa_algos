class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # given
        # arr
        # len of max size turb arr
        # turb in this case means adj elements are less than or more than but must be less -> more or more -> and swapping signs every time

        # intuition / brute force
        # we can use an approach where we iterate each item in the list
        # first we need to make sure we have two pointers that dont point to same item, since we want to compare 2 vals
        # first pointer pointers to 0th index, seocnd = 1st index
        # res var to store the len of the resulting arr
        # prev var to store prev sign
        # then find the subarrs starting from each index
        # calc the valid arrs and update vars and pointers as needed
        # need to check if arr[R] > arr[R - 1] # r - 1 would be prev index and need to check if the prev wasnt a ">"
        # then we can update res with the max of the curr res val and the curr length, which would be R - L + 1
        # then move r to the rght
        # then update prev
        # then we need the opposite case
        # then we have the outstanding case
        # where if the sign is = or if the sign is repeated
        # we update R to be next index IFF curr index equal to prev else R same
        # L is always R - 1, prev index
        # set prev to empty val
        # time = O(n)
        # space = o(1)

        # implement
        L, R = 0, 1
        res, prev = 1, "" # given res will be min of 1 guarantee from constraint

        while R < len(arr):
            if arr[R] > arr[R - 1] and prev != ">":
                res = max(res, R - L + 1) # R - L + 1 includes r to l length subarr
                R += 1 # to the right
                prev = ">"
            elif arr[R] < arr[R - 1] and prev != "<":
                res = max(res, R - L + 1)
                R += 1
                prev = "<"
            else:
                R = R + 1 if arr[R] == arr[R - 1] else R # we move right one if indices same val
                L = R - 1
                prev = ""

        return res