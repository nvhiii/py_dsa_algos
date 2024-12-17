class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # given
        # nums circular arr of len n
        # max sum is to be returned
        
        # intuition / brute force
        # since we know a brute force to finding max in a noncircular linked list is iter each item in list then calc sum of each subarr then compare to max
        # this is o(n^2), hence we use kadanes for a one pass to ignore negative values
        # in our case, we can use this logic for the items in the middle, ignoring the circular aspect of list atm
        # globalMax, currMax to compare the maximums
        # iteration needed via one pass to calculate max
        # we can easily find the max in the middle this way, and since we know it is the max in the middle, why cant
        # we just say the rest of the list is the global min? actually instead of guessing, we can track global min as well
        # globalMin, currMin to compare mins
        # we iterate the loop and continuously update min and max globally
        # we can calc global max vs the global min and substract it from the total of the arr and compare the two, whichever
        # is larger is the max Sum
        # however, we have one edge case of what if the entire arr all negative vals?
        # we add a check on the return if glboalMax > 0 else return the globalMax, since that will be the max if all nums are neg
        # time = o(n) since one pass iteration of nums
        # space = o(1) since no arr instantiated

        # global max, global min
        # curr max, curr min
        # total

        gmax, gmin = nums[0], nums[0]
        cmax, cmin = 0, 0
        total = 0
        for n in nums:
            cmax = max(cmax, 0)
            cmax += n
            cmin = min(cmin + n, n)

            # update gmax and gmin
            gmax = max(gmax, cmax)
            gmin = min(gmin, cmin)

            # inc total
            total += n

        return max(gmax, total - gmin) if gmax > 0 else gmax