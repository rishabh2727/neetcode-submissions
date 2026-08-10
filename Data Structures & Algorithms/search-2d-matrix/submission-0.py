class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # I have a matrix, which is 2d array
        # binary search
        # left = matrix[0][0]
        # right = matrix[-1][-1]
        # example, mid = 20, I have to check all rows
        # and see which row's last element is bigger than mid
        # once I find that, I eliminate all other rows
        # how to iterate through only the rows
        # for row in matrix:
        #     here row is an array
        #     check last element
        #     if mid <= row[-1]
        #         eliminate rows that come after this one
        #     how to know which row is this?
        #     figure out which row is my target potentially in?

        # number of rows = 3
        # search space is 0-3
        # find middle row, check its last element 
        left = 0
        right = len(matrix)-1
        # 0,2 = mid = 1

        while left < right:
            mid = (left+right)//2
            if target > matrix[mid][-1]:
                left = mid+1
            else:
                right = mid
        
        for r in matrix[left]:
            if r == target:
                return True
        
        return False
        

        
            
        
        