class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array, then to find three numbers that add up
        # to zero, num1 + num2 = - num3
        # num3 becomes a target. 
        # so after sorting array will be
        #  left at one end . right at the other
        #  now if left + right > target, right --
        #  else left ++
            #  [-4,-1,-1, 0, 1, 2]
            # nums[left] = -4
            # nums[right] = 2
            # target = 2
            # loop from 1,
        nums.sort()

        triplets = []
        # first fix the number , then find the pairs, that is where you 
        # can apply the logic, for moving the left and right pointer 
        # depending on nums[j] + nums[k] > or < than target
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            target = -nums[i]
            while left < right:
                sum = nums[left]+nums[right]
                if sum == target:
                    triplets.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1

        return triplets


                
        

        
        
        