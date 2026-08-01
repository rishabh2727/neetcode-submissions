class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # what did I do wrong
        # did not use copy() to append cur_lst to lst
        # I dont move pointers correctly, after loop finished
        # it was still possible to shrink the window, but right
        # reached the end of array.
        # always expand the window first, and then shrink it.
        # separate out the logic clearly.

        cur_sum = 0
        res = float("inf")
        left,right = 0, 0
        while right < len(nums):
            cur_sum += nums[right]
            while cur_sum >= target:
                print("Current_SUm", cur_sum)
                print("Array Size", right-left+1)
                res = min(res,right-left+1)
                print(res)
                cur_sum -= nums[left]
                left += 1
            right += 1
  
        return res if res < float("inf") else 0










        