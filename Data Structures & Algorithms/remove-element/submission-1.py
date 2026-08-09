class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # write pointer. which will on the left
        # read pointer that iterates through the array
        # and finds element not equal to val, so that we 
        # swap values with write when write pointer has value = val

        # nums = [3,2,2,3], val = 3

        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1

        return write



        # [3,3,3,3,2,4,5]
        # read = 3, write = 3
        # while write == 3, skip 
        # makes write = 2
        # swap, [2,4,5,3,3,3,3]
        # write = 4 
        # read = 3(index 1)



        