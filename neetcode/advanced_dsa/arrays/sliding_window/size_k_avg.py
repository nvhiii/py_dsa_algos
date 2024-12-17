class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # given
        # arr of int
        # k = expected size of subarr + avg must be greater than or equal to threshold >=
        
        # ambiguities
        # any way you want me to solve this problem specifically?

        # intuition / brute force
        # have a var to hold num of subarrs that fit our constraint
        # have 2 pters for nested loop
        # have curr sum for each iter in L pointer
        # update using R pointer
        # then check if its in the constraint
        # time: o(n squared) / space: o(1) # bc no extra ds needed

        # approach / optimization
        # store num of subarr that fit constraint, res
        # sum the first k - 1 elements, to make easy to iterate loop, this is our currSum var
        # iterate using 1 left pointer through range of entire arr minus k + 1, this is intuitive, so we have exactly k sized subarrs only
        # inc currSum
        # check if that currSum fits the threshold
        # inc if it does
        # then every iteration, slide the window over
        # return result after exiting the loop
        # time = O(n) since one pass iteration of loop
        # space = O(1) since no extra memory allocation, not significant at least

        res = 0
        currSum = sum(arr[:k - 1]) # k = 3, will get :3

        for L in range(len(arr) - k + 1):
            currSum += arr[L + k - 1] # adds last item of the window only
            if currSum / k >= threshold:
                res += 1
            currSum -= arr[L]

        return res