class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, n):
            curr = nums[i]

            if curr > currSum:
                if currSum > 0:
                    currSum = currSum + curr
                else:
                    currSum = curr
            else:
                currSum = curr + currSum

            maxSum = max(currSum, maxSum)
            
        return maxSum

