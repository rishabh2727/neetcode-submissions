class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid +1
            else:
                right = mid -1

        return left
        


        # [-1,0,2,4,6,8] left = 0, right = 5, mid = 2
        # [-1,0,2,4,6,8,9] left = 0, right = 6, mid = 3
        # does left and right eventually point to same index 
        # after while loop is over
