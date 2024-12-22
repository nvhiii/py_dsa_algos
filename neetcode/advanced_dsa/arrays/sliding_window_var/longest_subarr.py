class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # given
        # string s
        # find length of longest substr w no repeating char

        # intuition
        # what do we need to track?
        # need to L and R pointers to track which chars we are at, what we need to remove until we make set not have dupes etc
        # finding dupes, so prob a set for efficient accessing in constant time
        # lengths own var
        # iterate whole len str w right pointer
        # check while s[R] in window
        # remove s[L] from window
        # inc L by 1
        # add the curr char to the window
        # update length
        # return length
        # time: o(n)
        # space: o(n)

        window = set()
        length = 0
        L = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L]) # least reccent idx item in set
                L += 1
            window.add(s[R])
            length = max(length, len(window))

        return length