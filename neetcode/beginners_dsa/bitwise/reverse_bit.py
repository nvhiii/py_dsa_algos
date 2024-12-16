class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32): # 32 bit int
            bit = (n >> i) & 1 # get each bit
            res = res | (bit << (31 - i)) # we shift each bit the opposite direction it was added from
        return res