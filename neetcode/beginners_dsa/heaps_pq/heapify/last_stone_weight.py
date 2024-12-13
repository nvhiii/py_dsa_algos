class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # notes
        # stones arr w/ weights
        # 2 heaviest stones per iter
        # case to smash
        # want to return 1 stone at end (or 0)
        # mismatch = always smash and append

        # brute force
        # sort the stones arr, then reverse iterate from end. O(n) operation
        # then we append too, o(1) tho.
        # could be better, say we use min heap
        # o(n) for heapify
        # then we access in logn

        stones = [-s for s in stones] # mimic max heap using negation
        heapq.heapify(stones) 

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y) # we append x - y bc the values are negated in our arr

        return -stones[0] if stones else 0