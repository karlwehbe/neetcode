class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n

        for i in range(n):
            if i == 0 or i == 1:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i - 3] + nums[i], dp[i - 2] + nums[i])
        
        return max(dp[-1], dp[-2])


        [2, 1, 1, 2]

        [2, 1, 3, 4]

        dp[3] = max(nums[3] + nums[i-2], )