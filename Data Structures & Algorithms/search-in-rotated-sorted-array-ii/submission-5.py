class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1

        # [3,4,5,6,0,1,2], mid = 5,left = 5, right = 2
        # [1,0,1,1,1] mid = 1, left = 1, right = 1, target = 0

        while left <= right:
            while left+1 <= right and nums[left] == nums[left+1]:
                left += 1   
            while right-1 >= left and nums[right] == nums[right-1]:
                right -= 1
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            # right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid-1
        
        return False
            

            



            

            


        
        return False
            
        