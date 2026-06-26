from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      solution = []
      count = {}
         
      for num in nums:
        if num in count:
          count[num] += 1
        else:
          count[num] = 1

      keys = list(count.keys())
      values = list(count.values())

      print(keys)
      print(values)

      k_biggest_values = [0 for i in range(k)]
      for i in range(len(values)):
        key = keys[i]
        val = values[i]
        if val > min(k_biggest_values):
            k_biggest_values[k_biggest_values.index(min(k_biggest_values))] = val
        
      
      print(k)
      for val in k_biggest_values:
        idx = values.index(val)
        solution.append(keys[idx])
        keys.pop(idx)
        values.pop(idx)

      return solution


