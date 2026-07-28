class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,3,4,5,8,9]
        # target = 9
        # return [4,6]
        left = 0
        right = len(numbers)-1
        while left < right:
            sum = numbers[left]+ numbers[right]
            if sum == target:
                return [left+1,right+1]
            elif sum > target:
                right -= 1
            else:
                left += 1
        









        