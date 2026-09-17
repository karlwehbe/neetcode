import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distances = []
        
        for p in points:
            d = math.sqrt(p[0] * p[0] + p[1] * p[1])
            distances.append((d, p))
        
        print(distances)
        
        heapq.heapify(distances)

        closest = heapq.nsmallest(k, distances)

        print(closest)

        for p in closest:
            res.append(p[1])
        
        return res

