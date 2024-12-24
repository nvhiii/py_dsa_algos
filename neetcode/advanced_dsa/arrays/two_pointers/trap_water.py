class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        L, R = 0, len(height) - 1
        ml, mr = height[L], height[R]
        water = 0

        while L < R:
            if ml < mr:
                L += 1 # increment left until its not minimum of left and right max
                ml = max(ml, height[L]) # we calc the max of the left bound
                water += ml - height[L] # we first substract index at L from the left bound, since right max 
                #doesnt matter, since its already guaranteed to be less than the right bound, 
                #and that min determines the limit of water to hold, hence
                # we do ml - curr index val
            else:
                # same logic as above
                R -= 1
                mr = max(mr, height[R])
                water += mr - height[R]

        return water