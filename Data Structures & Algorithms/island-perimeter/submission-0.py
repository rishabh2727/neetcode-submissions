class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # find all cells connected together
        # check four directions, how to count the sides?

        # how to count the number of cells in the island?
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()


        def dfs(row,col):
            count = 0
            # base case
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return 1
            if (row,col) in visited:
                return 0
 
            visited.add((row,col))

            
            for rr, cc in directions:
                nr = row+rr
                nc = col + cc

                count += dfs(nr,nc)
            
            return count
            

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r,c)

        


 


