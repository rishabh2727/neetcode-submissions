class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(temp,open,closed):
            if open == n and closed == n:
                str_temp = "".join(temp)
                res.append(str_temp)
                return
            if open < n:
                temp.append('(')
                dfs(temp, open+1,closed)
                temp.pop()

            if closed < n and closed < open:
                temp.append(')')
                dfs(temp,open,closed+1)
                temp.pop()


        dfs([],0,0)
        return res





# if n = 2
# means two open two closed brackets needed, generate all such combintations
# dfs([],0,0) A
#     dfs("(", 1,0)  B 
#         dfs("((",2,0). C
#             dfs("(()",2,1) D
#                 dfs("(())",2,2) -> return  E
#         dfs("()",1,1)   
            









# at every stage/root,we have two choices, either add the () inside
# of the existing one, making it nested. or adding it as a seprate bracket
#         how many parantheses can I generate with one?
#         1 pair, is ()
#         2 pairs - ()() (())
#         3 pairs - ()()(), (())(), ()(()), ((())) 4 pairs
#         n =3
#         dfs("()", 1)
#             dfs("(())",2)
#                 dfs("((()))",3) -> return 
#                 dfs("(())()",3) -> return
#             dfs("()()",2)
#                 dfs("()(())",3) -> return
#                 dfs("()()()",3) -> return 

# how to generate all substrings?


        