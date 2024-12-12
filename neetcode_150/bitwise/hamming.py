class Solution:
    def hammingWeight(self, n: int) -> int:
        # return num of bits given a int
        count = 0
        while n > 0:
            if n & 1 == 1: # truthy bc we check if last val is a 1, 2^0
                count += 1
            # decrement the num by a factor of 2,  bitwise move right /2
            n = n >> 1
        return count