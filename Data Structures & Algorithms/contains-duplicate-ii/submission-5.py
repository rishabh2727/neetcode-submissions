class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # why use a hash set?
        # make an empty set = {}
        # [1,2,3,1]
        # k creates a window, only check elements within that

        # [1,2,3,4,5,2,1,2] k = 2
        # window = 
        # 1-3
        # 2-4
        # 3-5
        left = 0
        myset = set()
        # using window technique, distance between left and right
        # pointers is fixed in this case, only save the elements in the
        # current window in the set, if the new element already exists
        # in the set, it means it is within that distance, and we return 
        # True. the check for number of elements in the set currently
        # has to be first, since we cannot add the current nums[right] and
        # exceed the window size. 
        for right in range(len(nums)):
            if right - left > k:
                myset.remove(nums[left])
                left += 1
            if nums[right] in myset:
                return True
            myset.add(nums[right])
            
                
        return False












        # mydict = {}
        # for i in range(0,len(nums)):
        #     if nums[i] in mydict and abs(mydict[nums[i]]-i) <= k:
        #         return True
        #     mydict[nums[i]] = i
        
        # return False



        # for i in range(0,len(nums)):
        #     for j in range(i+1, min(len(nums),i+k+1)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False







        