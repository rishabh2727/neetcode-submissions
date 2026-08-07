import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      
        #  1          4        3        2
        # pile1     pile2.   pile3.   pile4

        # I have 9 hours to eat the bananas = h

        # try to minimize the eating rate k, but finish within 
        # 9 hours(h)

        # try 1 banana per hour
        # try 2 bananas per hour

        # how to test if speed of 1 works?

        # go through all piles, check how many bananas
        # hours = 0
        # hours += piles[i]

        # then if hours > h:
        # do the calculation again
        # function that checks if current speed for eating bananas
        # is sufficient to finish within h hours, if 
        # yes, return a boolean value, thats all
        def binary_search(cur_speed, piles):
            hours = 0
            for p in piles:
                hours += math.ceil(p / cur_speed)
            if hours <= h:
                return True
            return False
        
        right = max(piles) 
        left = 1
        min_hours = max(piles)
        # only iterate over speed from range 1 to max
        # using binary search to divide the searching space
        while left < right:
            mid = (left+right) // 2
            if binary_search(mid, piles):
                min_hours = min(min_hours, mid)
                right = mid
            else:
                left = mid+1
        
        return min_hours




# do binary search on the speed itself, the max speed possible
# is max(piles), start with 1, and then find mid = 1+max(piles)//2
# try with this current speed, if it works, return speed
# else if speed is not enough, go to the other half.
# coming up the structure.











        