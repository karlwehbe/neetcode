class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        leftMost = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            
            stack.append(i)

        rightMost = [n] * n
        stack = []
        for i in reversed(range(n)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            
            stack.append(i)

        maxArea = 0
        for i in range(n):
            print(rightMost[i], leftMost[i])
            maxArea = max(maxArea, heights[i] * ((rightMost[i] - 1) - (leftMost[i] + 1) + 1))
        
        return maxArea