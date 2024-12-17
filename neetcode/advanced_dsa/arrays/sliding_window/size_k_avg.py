class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # track res
        # then track the first k - 1 sum
        res = 0
        currSum = sum(arr[:k - 1]) # sums first k - 1 elements, smart to do beofre iteration

        for L in range(len(arr) - k + 1):
            currSum += arr[L + k - 1] # add next val only of the window
            if currSum / k >= threshold:
                res += 1
            # slide window
            currSum -= arr[L]

        return res