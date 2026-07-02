class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_idx = stack.pop()
                solution[prev_idx] = i - prev_idx

            stack.append(i)
            
        return solution