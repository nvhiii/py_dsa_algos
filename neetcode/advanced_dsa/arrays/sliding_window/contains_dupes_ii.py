class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # given
        # arr nums
        # return bool if distinct indices with same value
        window = set()
        L = 0
        for R in range(len(nums)):
            # check if window is k size
            if R - L > k:
                window.remove(nums[L])
                L += 1
            # check if it exists dupe
            if nums[R] in window:
                return True

            # add to window
            window.add(nums[R])

        # if iteration happend and not a single true
        return False