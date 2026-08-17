class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                product *= n
        
        if zeros >= 2:
            return [0]*len(nums)

        if not zeros:
            for i in range(len(nums)):
                nums[i] = product//nums[i]
        else:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
        
        return nums