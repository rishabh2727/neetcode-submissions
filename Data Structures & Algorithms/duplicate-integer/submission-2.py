class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        # TC: will be O(n), go through every element to create a set
        # SC: O(n), to store the set, worst case, all elements are different
        # and all of them have to be stored in set in memory, 

        

    

            