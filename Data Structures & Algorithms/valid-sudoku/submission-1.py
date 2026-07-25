class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # how to look for duplicates in a row?
        # checking for rows using dict
        mydict = {}

        for row in board:
            mydict.clear()
            for r in row:
                if r.isdigit():
                    if r not in mydict:
                        mydict[r] = 1
                    else:
                        return False

        # we are talking about the first element of every row.
        # and then the second and so on.
        seen = set()
        col = 0
        while col < 9:
            for row in range(9):
                # put them in a set, if it repeats return False
                element = board[row][col]
                if element != ".":
                    if element not in seen:
                        seen.add(element)
                    else:
                        return False
            col += 1
            seen.clear()

        seen = set()
            # 9 boxes, 9 elements in each box, check elements are different
        for box in range(9):
            starting_row = box//3 * 3
            starting_col = box%3 * 3
            seen.clear()
            for row in range(starting_row, starting_row+3):
                for col in range(starting_col, starting_col+3):
                    element = board[row][col]
                    if element != ".":
                        if element not in seen:
                            seen.add(element)
                        else:
                            return False
        return True
                        

# you want the row and col to be those exact values like 0,3
# and then change them to - row - 0,3 col - 3,6 for box 2
# box 3 - row - 0,3 , col - 6,9
# box 4 - row - 3,6, col - 0,3
# so you see a pattern, come up with a formula for the rows and 
# columns.

        
# look at the box number for every starting row, it will be 
# box 0
# box 3
# box 6
# so here, if I divide box number by 3, it will tell me which row is box in

# look at box number for every column(rightwards)
# box 0, box 1, box 2
# box 3, box 4, box 5
# here, to find column number for the box, if I do %3 i can tell.