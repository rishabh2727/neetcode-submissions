class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_car = []
        for i in range(len(position)):
            time = (target-position[i])/speed[i]
            time_car.append((position[i],time))

        stack = sorted(time_car)
        fleets = 0

        while stack:
            pos, T = stack.pop()
            fleets += 1
            while stack and stack[-1][1] <= T:
                    # add this car to the fleet, and pop this as well
                    stack.pop()

        return fleets
            


        
        # when is a car fleet formed, if two cars reach at the same time.
        # if their time to reach is same, then they form a fleet
        # but if speed of car behind is more, then time to reach might be 
        # even quicker than the car ahead of it, in this case, we have to 
        # still form a fleet, since car cannot pass the car ahead of it.

        # process the time_car array from behind. 
        # [2, 3 ,4, 4.5, 10.0, 3.0]
        # save the position as well
        # stack = 



        
        