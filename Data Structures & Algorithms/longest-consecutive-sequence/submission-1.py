class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
            















        
        