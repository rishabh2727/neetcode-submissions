class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # modifying the array in place.
        # nums=[1,1,2,3,4]
        # nums=[2,10,10,30,30,30]
        left = 0
        for right in range(0,len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        
        return left+1









            
    






        