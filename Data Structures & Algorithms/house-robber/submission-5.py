class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, n):
            if i == 2:
                dp[i] = dp[0] + nums[i]
            else:
                dp[i] = max(dp[i - 3], dp[i - 2]) + nums[i]

        return max(dp[-1], dp[-2])