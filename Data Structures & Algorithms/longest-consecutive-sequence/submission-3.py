class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # without sorting
        numSet = set(nums)
        # nums=[2,20,4,10,3,4,5]
        # [3,2,5,4,6,1,1]
        longest = 0
        for num in nums:
            if num-1 not in numSet:
                # this is beginning of a sequence
                curr = 0
                number = num
                while number in numSet:
                    curr += 1
                    number += 1
                longest = max(curr, longest)

        return longest
        

















        # example = [0, 1, 1, 2, 3, 4, 5, 6]
        if not nums:
            return 0
        nums = sorted(nums)
        curr, longest = 1, 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                curr += 1 
                print(curr) 
            else:
                curr = 1
            longest = max(longest,curr)

        return longest
            















        
        