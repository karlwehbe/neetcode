import copy 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0 for i in range(len(temperatures))]        
        idx = 0

        while len(temperatures) > 0:
            curr_temp = temperatures.pop(0)
            print(curr_temp, temperatures)
            for i in range(len(temperatures)):
                print(temperatures[i])
                if temperatures[i] > curr_temp:
                    solution[idx] = i + 1
                    break
            
            idx += 1

        return solution            

