class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = {0:1}
        res = 0

        running_total = 0
        for n in nums:
            running_total += n
            diff = running_total - k
            res += prefix.get(diff,0) 
            if running_total in prefix:
                prefix[running_total] += 1
            else:
                prefix[running_total] = 1
        
        return res




        
# nums = [2,-1,1,2]
# i = 0, j = 1 (positions/index)
# i:j = nums[0:1] = 2 == 2, count = 1

# i = 0, j= 2




    


# you would have to go through all the subarrays
# two nested loops
