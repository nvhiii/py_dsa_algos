class Solution:
    def isPalindrome(self, s: str) -> bool:
        # given
        # string s
        # return bool val if palindrome

        # brute force intuition
        # create arr to store str and compare it with its reverse
        # space will be 2 * n
        # time = o(n)

        # optimized:
        # keep in mind the string may be "dirty", so need to convert to only alnum + lower
        # use 2 pointers from first string char to last string char
        # if chars != equal, immediately return false
        # if entire iteration done, then retunr True

        s = "".join(char.lower() for char in s if char.isalnum())
        # need to reformat string first
        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1

        return True