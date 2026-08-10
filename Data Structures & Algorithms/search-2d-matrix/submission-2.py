class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # I have a matrix, which is 2d array
        # binary search
        # I have to check all rows
        # and see which row's last element is bigger than mid
        # once I find that, I eliminate all other rows
        # how to iterate through only the rows
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
        
        row = left
        low = 0
        high = len(matrix[row])-1
        print(low,high)

        while low <= high:
            middle = (low+high)//2
            if matrix[row][middle] == target:
                return True
            elif target > matrix[row][middle]:
                low = middle+1
            else:
                high = middle-1

        return False
        

        
            
        
        