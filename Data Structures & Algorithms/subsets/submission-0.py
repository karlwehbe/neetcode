class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        if not nums:
            return res
        
        stack = []
        def dfs(idx):
            print(idx, stack)
            if idx == len(nums):
                res.append(stack.copy())
            
            else:
                stack.append(nums[idx])
                dfs(idx + 1)

                stack.pop()
                dfs(idx + 1)

        dfs(0)

        return res
        

    #         [1]             []
    #      []     [2]       []  [2]
    #    [] [3]  [] [3]   [] [3] [] [3]
    # [1]  [1,3] [1,2] [1,2,3]