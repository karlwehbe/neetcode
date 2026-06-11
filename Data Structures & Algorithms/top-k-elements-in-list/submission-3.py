from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
          if num in count:
            count[num] += 1
          else:
            count[num] = 1

        pairs = list(count.items())
        inverse_pairs = [(count, element) for element, count in pairs]
        heapq.heapify(inverse_pairs)
        
        k_most_frequent = heapq.nlargest(k, inverse_pairs)
        frequency = [element for count,element in k_most_frequent]
        return frequency







