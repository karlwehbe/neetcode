class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        if not nums:
            return res
        
        def dfs(idx, remain):
            if remain == 0:
                res.append(combination.copy())
                return

            else:
                for i in range(idx, len(nums)):
                    combination.append(nums[i])
                    diff = remain - nums[i]
                    if diff >= 0: 
                        dfs(i, diff)
                   
                    combination.pop()

        dfs(0, target)
        return res



    #                   [3]           16 - 3 = 13
    # 13 - 3 = 10 [3]         [4]         13 - 4 = 9
    #         [3][4][5]    [3][4][5]
    # 10 - 3 = 7           9 - 3 = 6  
    # 10 - 4 = 6           9 - 4 = 5
    # 10 - 5 = 5           9 - 5 = 4

    # [3][4][5] [3][4][5] [3][4][5]