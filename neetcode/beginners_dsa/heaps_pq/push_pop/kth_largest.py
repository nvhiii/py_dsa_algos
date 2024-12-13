import heapq

class Heap:
    def __init__(self, nums, k):
        self.k, self.nums = k, nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val):
        heapq.heappush(val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]