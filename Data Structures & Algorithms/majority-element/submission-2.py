import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        for n in nums:
            mp[n] = mp.get(n,0) + 1
            if mp[n] > math.floor(len(nums)/2):
                return n
 

        




        

        