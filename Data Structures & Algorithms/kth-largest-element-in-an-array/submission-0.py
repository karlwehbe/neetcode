import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = 0

        if not nums:
            return largest
        
        max_heap = [-n for n in nums] # O(n)

        heapq.heapify(max_heap) # O(n)

        counter = 0
        while True: 
            kth = heapq.heappop(max_heap)

            counter += 1

            if counter == k:
                return -kth



