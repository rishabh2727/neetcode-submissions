class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mydict = {}
        for i in range(0,len(nums)):
            if nums[i] in mydict and abs(mydict[nums[i]]-i) <= k:
                return True
            mydict[nums[i]] = i
        
        return False



        # for i in range(0,len(nums)):
        #     for j in range(i+1, min(len(nums),i+k+1)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False







        