class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 3:
            return max(nums)

        n = len(nums) - 1
        temp = nums.pop(-1)
        
        dp1 = [0] * n 
        for i in range(n):
            if i == 0 or i == 1:
                dp1[i] = nums[i]
            else:
                dp1[i] = max(dp1[i - 3] + nums[i], dp1[i - 2] + nums[i])

        nums.append(temp)
        nums.pop(0)
        dp2 = [0] * n
        for i in range(n):
            if i == 0 or i == 1:
                dp2[i] = nums[i]
            else:
                dp2[i] = max(dp2[i - 3] + nums[i], dp2[i - 2] + nums[i])


        return max(max(dp1), max(dp2))