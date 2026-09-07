class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        best = sum(nums)
# nums=[1,0,2,3,5], left = 5, right = 11,mid = 8
# k=4 
# # nums=[2,4,10,1,5]
# k=2, left = 10, right = 22, mid = 16, 

        def binary(left, right):
            # function to see if mid value is valid and passes or not
            nonlocal best
            while left <= right:
                mid = (left+right)//2
                if search(mid,k-1):
                    best = mid
                    right = mid-1
                else:
                    left = mid+1
        
            return best

        
        def search(mid,m):
            cur_sum = 0
            for i in range(len(nums)):
                if cur_sum + nums[i] <= mid:
                    cur_sum += nums[i]
                else:
                    m -= 1
                    if m < 0:
                        return False
                    cur_sum = nums[i]
            return True

        return binary(max(nums),sum(nums))



        # check if we can make k subarrays where largest sum of any subarray
        # is less than mid, greedy approach.
        # we can create a new subarray if sum exceeds, but we can only
        # create m subarrays
    # nums = [2,4,10,1,5], k = 2
    # left = 10, right = 22, mid = 16

    # search(16,2)   
    # cur_sum = 6
    # m = 1

                

        

        