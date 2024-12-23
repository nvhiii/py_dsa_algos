class Solution:
    def maxArea(self, height: List[int]) -> int:
        # move pointers from left and right
        L, R = 0, len(height) - 1
        maxArea = 0

        while L < R:

            width = R - L
            area = min(height[L], height[R]) * width

            maxArea = max(maxArea, area)

            # move smaller height
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return maxArea