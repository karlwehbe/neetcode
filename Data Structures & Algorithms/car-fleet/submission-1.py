class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_data = [[pos, spd] for pos, spd in zip(position, speed)]        
        car_data.sort(reverse=True)

        fleet_count = 0

        stack = []

        print(car_data)

        car_time = []
        for car in car_data:
            time = (target - car[0]) / car[1]
            car_time.append(time)
        
        print(car_time)

        stack = []
        for time in car_time:
            # If stack is empty or this car takes LONGER than the fleet ahead
            if not stack or time > stack[-1]:
                stack.append(time)
        # The number of fleets is the size of the stack
        return len(stack)
                

