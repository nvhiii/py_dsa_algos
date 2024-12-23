class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # given
        # arr of numbers in non decreasing order, meaning there can be dupes
        # find two numbers that add up to exactly target
        # return the indices of both numbers (cannot be same index)
        # also since we using 1 indexing, add 1 at the end when returning val for ease

        L, R = 0, len(numbers) - 1
        while L < R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            else:
                return [L + 1, R + 1] # guaranteed one solution