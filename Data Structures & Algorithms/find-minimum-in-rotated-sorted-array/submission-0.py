class Solution:
    def findMin(self, nums: List[int]) -> int:
# [3,4,5,6,1,2]
#  left = 3, right = 2 ,mid = 5,
#  left = 6, right = 2, mid = 1
#  
        left = 0
        right = len(nums)-1
        minimum = float("inf")

        while left <= right:
            mid = (left+right)//2
            minimum = min(nums[mid], minimum)
            if nums[mid] < nums[right]:
        # it means both mid and right belong to the right
        # sorted segment, and minimum element is in left half
                right = mid-1

            else:
        # it means left and mid are in same sorted segment,
        # so minimum element is in the other half.
                left = mid+1
        return minimum









        
        