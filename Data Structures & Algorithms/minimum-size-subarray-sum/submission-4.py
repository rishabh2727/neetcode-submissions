class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        cur_lst = []
        lst = []
        left,right = 0, 0
        while right < len(nums):
            cur_lst.append(nums[right])
            right += 1
            while sum(cur_lst) >= target:
                lst.append(cur_lst.copy())
                cur_lst.pop(0)

        if not lst:
            return 0
            
        min_len = len(lst[0])
        for sub in lst:
            min_len = min(min_len, len(sub))

        return min_len



            








        # l , r
        # [l:r] is subarray, 
        # take a lst, append all passing subarrays to it,
        # then go through lst, and find the smallest(one with least elements)


        