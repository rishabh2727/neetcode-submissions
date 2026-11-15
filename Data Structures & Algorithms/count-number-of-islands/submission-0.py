from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # how to iterate a grid in graphs, this is a type of 
        # question in graphs.
        row = len(grid) #rows
        col = len(grid[0]) #cols
        queue = deque()
        # we would stop when all cells in the matrix
        # have been visited, I am guessing
        # visited = [[0]*col]*row
        visited = [[0 for _ in range(col)] for _ in range(row)]
        print(visited)

        count = 0

        def bfs(i, j):
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                x, y = queue.popleft()
                # top
                if x - 1 >= 0 and grid[x-1][y] == "1" and visited[x-1][y] == 0:
                    queue.append((x-1, y))
                    visited[x-1][y] = 1
                # bottom
                if x + 1 < row and grid[x+1][y] == "1" and visited[x+1][y] == 0:
                    queue.append((x+1, y))
                    visited[x+1][y] = 1
                # left
                if y - 1 >= 0 and grid[x][y-1] == "1" and visited[x][y-1] == 0:
                    queue.append((x, y-1))
                    visited[x][y-1] = 1
                # right
                if y + 1 < col and grid[x][y+1] == "1" and visited[x][y+1] == 0:
                    queue.append((x, y+1))
                    visited[x][y+1] = 1

        
        for i in range(row):
            for j in range(col):
                # it means that the cell either has
                # water or it has been visited already
                if grid[i][j] == "0" or visited[i][j] == 1:
                    continue
                # call bfs here, starting point is important
                bfs(i,j)
                count += 1

        return count
                
                    


        # only logic to apply :
        # here two nodes are connected if there is a 1 in
        # either top, bottom, left or right cell
        # and then we can consider them the neighbours
        # and append them to the queue, add them to visited
        # if not connected, we start another traversal at
        # that node, and add one to outr island
        # look for the 1st one in our grid and start from there
        # the starting point is a bit tricky.

