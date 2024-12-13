# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSort_helper(pairs, 0, len(pairs) - 1)

    def mergeSort_helper(self, pairs: List[Pair], s, e):
        if e - s + 1 <= 1:
            return pairs

        mid_idx = (s + e) // 2
        self.mergeSort_helper(pairs, s, mid_idx)
        self.mergeSort_helper(pairs, mid_idx + 1, e)

        self.merge(pairs, s, mid_idx, e)

        return pairs

    def merge(self, pairs: List[Pair], start, middle, end):
        L = pairs[start : middle + 1]
        R = pairs[middle + 1 : end + 1]

        i = 0 # tracks idx of L
        j = 0 # tracks idx of R
        k = start # tracks relevant start idx of arr

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key: # this is relative order conscious
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1 # k will increment with both cases

        # if one arr longer than the other, need to exhaust it
        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1
