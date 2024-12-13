from math import ceil

class Solution:
    # h is the hour limit to be in
    # k is what we solve for, ban per hr, if k greater than piles[i], finish pile but cannot move on
    # find min k
    # therefore, h must be greater or equal to max of pile in piles
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r # worst case banana eating rate
        while l <= r:
            # k calc
            k = l + (r - l) // 2
            hourSpent = 0 # for given K eating banana rate, how long to eat all bananas in all piles
            for pile in piles:
                hourSpent += math.ceil(float(pile) / k)
            if hourSpent <= h: # must be less than or equal to because we must do WITHIN the range, inclusive implied
                # case where we are in time limit and finished the bananas
                res = k
                # since we are iterating through 1 - max(piles), we want to decrement the r bound
                r = k - 1
            elif hourSpent > 1:
                l = k + 1
        return res