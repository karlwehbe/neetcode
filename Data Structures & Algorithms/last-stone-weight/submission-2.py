import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:

            x = heapq.heappop(max_heap) * -1
            y = heapq.heappop(max_heap) * -1

            diff = x - y
   
            if diff > 0:
                heapq.heappush(max_heap, -diff) 

        if len(max_heap) == 1:
            return -max_heap[0]
        
        return 0
