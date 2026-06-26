from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      solution = []
    
      count = Counter(nums)

      keys = list(count.keys())
      values = list(count.values())

      k_biggest_values = [0 for i in range(k)]
      for i in range(len(values)):
        key = keys[i]
        val = values[i]
        if val > min(k_biggest_values):
            k_biggest_values[k_biggest_values.index(min(k_biggest_values))] = val
        
      
      for val in k_biggest_values:
        idx = values.index(val)
        solution.append(keys[idx])
        keys.pop(idx)
        values.pop(idx)

      return solution


