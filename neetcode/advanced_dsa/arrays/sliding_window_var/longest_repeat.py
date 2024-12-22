class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # given
        # stirng s
        # k operations of replacing, dont need to replace
        
        # brute force / intuition
        # what do we need to track
        # count of the charas
        # L and R pointers
        # maxFreq to substract to find complementary char val and check if it is less than and equal to k or not

        cc = {}
        L = 0
        maxFreq = 0

        for R in range(len(s)):

            # update the entry in the hm
            cc[s[R]] = cc.get(s[R], 0) + 1

            # update the max freq
            maxFreq = max(maxFreq, cc[s[R]])

            # check complementary val, if it cant be possible, move left pointer
            while (R - L + 1) - maxFreq > k:
                cc[s[L]] -= 1
                L += 1

        return R - L + 1