class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            version = low + (high - low) // 2
            if isBadVersion(version):
                high = version - 1
            else:
                low = version + 1
        return low