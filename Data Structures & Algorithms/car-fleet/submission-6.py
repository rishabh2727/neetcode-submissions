class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # how to find if two cars can catch upto each other?
        # how far apart is each car from target?

        # positions = [1,4]
        # how_far =   [9,6]
        # speed = [3,2]
        # how much time for car to reach = distance/speed
        # time[i] = (target - position[i]/speed[i]) = 3 hours
        # time[i] = 6/2 = 3 hours
        # both take same time so become a fleet
        
        # check for car fleets
        # once I have time:
        # position = [4,1,0,7,2,3]
        # time = [3,4.5,10,3,4,1] for every car to reach the target

        # 1 + 1 + 1 = 3

        # figure out how to group them togther

        # group all similar elements together
        cars = sorted(zip(position,speed), reverse = "True")

        slowest_time = 0
        fleets = 0

        for pos, sp in cars:
            time = (target - pos) / sp
            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets
                


        





        
        