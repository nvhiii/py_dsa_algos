class Solution:
    def hammingWeight(self, n: int) -> int:
        # given that its a 32 bit number
        # give num bits in this number
        count = 0
        while n > 0:
            if n & 1 == 1: # valid case, same bit at end
                count += 1
            n = n >> 1 # divide by 2 to the power of 1
        return count