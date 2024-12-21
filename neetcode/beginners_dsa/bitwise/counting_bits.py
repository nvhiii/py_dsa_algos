class Solution:
    def countBits(self, n: int) -> List[int]:
        # given num n, create arr 0 to n inclusive
        # make into base10
        # count num of 1 bits in each num
        
        # brute or intuition
        # first \each num per iter

        arr = []
        for j in range(n + 1):
            # calc the base 2 from base 10 here
            # count bits
            bits = 0
            while j > 0:
                bits += j & 1
                j = j >> 1 # div by power of 2
            arr.append(bits) # this iterates once after the 1 bits calc is done for the num j

        return arr
    
# not most optimal

