class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # figure out the search space, monotonic?
        # function that checks if our guess(mid) is correct?

        # find weight capacity
        # sum of all weights = max weight capacity we need to have
        # least could be 1
        # so divide this search space into half.
        # if 50?
        # check if 50 works?
        # Function capacity(50):
        # have to go in order,keep subracting from 
        # capacity, once it goes over capacity, add a day to it.
        # if works, try reducing capacity again, we want to minimize
        # if I can do all the weights with curr_capacity
        # within days given, return True
        # cur_capacity is how many weights I can process in one day
        # [3,2,2,4,1,4], left = 4, right = 16, mid = 10
        # [1,2,3,4,5,6,7,8,9,10]
        # left = 10, right = 55, mid = 32
        
        
        def capacity(capacity):
            curr = capacity
            cur_days = 1
            for w in range(len(weights)):
                curr -= weights[w]
                if curr < 0:
                    cur_days += 1
                    curr = capacity - weights[w]
            print(f"days done in for capacity={capacity}:", cur_days)
            return cur_days <= days

        left = max(weights)
        right = sum(weights)
        best = float("inf")

        while left <= right:
            mid = (left+right)//2
            if capacity(mid):
                best = min(best,mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return best
        




        