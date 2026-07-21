class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        left, right = 1, maxPile

        maxHours = float("-inf")
        curr_rate = 0

        print(f"We get {h} hours")

        print("piles =", piles)

        k = 0
        while left <= right:
            print(left, right)
            curr_rate = left + ((right - left) // 2)
            curr_hours = 0
            for p in piles:
                hours_needed = math.ceil(p / curr_rate)
                if hours_needed == 0:
                    hours_needed = 1
                curr_hours += hours_needed
            
            print(f"For rate: {curr_rate}, we get {curr_hours} hours and the prev max is {maxHours}")
            
            if curr_hours >= maxHours and curr_hours <= h:
                print("Updating k")
                k = curr_rate
                maxHours = curr_hours
            
            if curr_hours <= h:
                right = curr_rate - 1
            elif curr_hours > h:
                left = curr_rate + 1
        
        return k