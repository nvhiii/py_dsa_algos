# given
# arr nums
# calc sum of elements btwn left and right inc and left <= right

class NumArray:

    def __init__(self, nums: List[int]):
        # create prefix sum arr
        self.ps = []
        total = 0
        for n in nums:
            total += n
            self.ps.append(total) # populated, will only run once in grand scheme of things

    def sumRange(self, left: int, right: int) -> int:
        # to calc sum using a prefix sum, we substract right bound and left bound
        rb = self.ps[right]
        # dont include anything before left bound
        lb = self.ps[left - 1] if left > 0 else 0
        return rb - lb

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)