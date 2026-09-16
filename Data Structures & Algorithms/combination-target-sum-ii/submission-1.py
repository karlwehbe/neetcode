class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        candidates.sort()
        print(candidates)

        if not candidates:
            return res

        def dfs(idx, remain):
            if remain == 0:
                res.append(combination.copy())
                return
            
            else:
                for i in range(idx, len(candidates)):
                    if idx < i and candidates[i] == candidates[i-1]:
                        continue
                    combination.append(candidates[i])
                    diff = remain - candidates[i]
                    if diff >= 0:
                        dfs(i+1, diff)
                
                    combination.pop()

        dfs(0, target)

        return res
