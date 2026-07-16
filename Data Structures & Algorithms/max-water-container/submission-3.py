class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        maxWater = 0
        while left < right:
            maxWater = max(maxWater, (right - left) * min(heights[left], heights[right]))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWater