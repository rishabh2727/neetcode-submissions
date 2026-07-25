class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not any(nums):
            return nums

        product = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            product *= num
        
        if zeros >= 2:
            return [0]*len(nums)
        
        if zeros == 0:
            nums = [product//num for num in nums]

        else:
            nums = [product if n == 0 else 0 for n in nums]

        return nums



        