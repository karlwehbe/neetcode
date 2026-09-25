class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
    
        dp = [0] * (len(cost) + 1)   

        top = len(cost) 

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])


        return dp[top]