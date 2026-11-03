class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        mydict = {}
        def helper(temp, mydict):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in mydict:
                    continue
                mydict[nums[i]] = 1
                temp.append(nums[i])
                helper(temp,mydict)
                temp.pop()
                mydict.pop(nums[i])

        helper([], {})
        return res


            
            


        