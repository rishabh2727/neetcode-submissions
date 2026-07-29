class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        rotations = k % len(nums)
        if rotations == 0:
            return nums
        # now do the rotations and shift the element one position
        # to the right
        n = len(nums)-1
        while rotations:
            temp = nums[n]
            for i in range(n,0,-1):
                nums[i] = nums[i-1]

            nums[0] = temp
            rotations -= 1
        
        return nums

        


            



        
