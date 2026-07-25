class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        mydict = {}
        length = len(nums)
        for n in nums:
            if n not in mydict:
                mydict[n] = 1
            else:
                mydict[n] += 1
        
        print(mydict)
        for k in mydict:
            if mydict[k] > length//3:
                res.append(k)
        
        return res

            

        