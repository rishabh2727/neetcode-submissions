class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left and mid sorted and target in between
        # mid and right sorted
        # find which portion is sorted,
        # then check if target lies in between those
        # sorted values, if yes, eliminate other half
        left = 0
        right = len(nums)-1

        # [4,5,6,7,0,1,2], mid = 7,left = 4, right = 2

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
                # left half is sorted
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
        
        return -1
            

        


        
        