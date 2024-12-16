def guessNumber(self, n: int) -> int:
        low = 1
        high = n # we dont care about index here
        while low <= high:
            mi = low + (high - low) // 2
            if guess(mi) < 0: # if -1, too high
                high = mi - 1
            elif guess(mi) > 0: # too low
                low = mi + 1
            else:
                return mi