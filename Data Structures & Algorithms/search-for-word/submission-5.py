class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row,col,index):
            if board[row][col] != word[index]:
                return False
            
            if index == len(word)-1:
                return True
                
            visited.add((row,col))

            for pair in directions:
                nr = row+pair[0]
                nc = col + pair[1]
                if (nr,nc) not in visited and 0 <= nr < rows and 0 <= nc < cols:
                    if dfs(nr, nc, index+1):
                        return True
            visited.remove((row, col))
            return False

        rows = len(board)
        cols = len(board[0])

        visited = set()

        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False
        

# check all its four sides, if next letter of the word exists
#     for loop to check all its sides,
#     calculate that by taking the current row and current column
#     (1,0),(-1,0),(0,-1),(0,1)
#     once new cells are found, checked if within the board,
#     we check if any is equal to the next letter in the word.

# dfs(index, word, curr=C):
#     for loop all its sides:
#         if cell == word[index]
#             return dfs(cell)

# dfs(C)
#     dfs(A)
#         dfs(T) - return true or false






