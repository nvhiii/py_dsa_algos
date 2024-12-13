import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mh = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            mh.append([dist, x, y])
        
        # heapify
        heapq.heapify(mh)
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(mh)
            res.append([x, y])
        
        return res