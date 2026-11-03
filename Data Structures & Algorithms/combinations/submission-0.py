class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
#         the length of my lst has to reach k, and then I add it to my res.
#         same concept as subsets, combination sum

#         I have to pick and not pick again, until I reach k length, that is when 
#         I count is as a valid combination.
#         [1,2,3]
#         from every position we have upto n options available, so for loop 
        res = []
        def dfs(lst,start):
            if lst and len(lst) == k:
                res.append(lst[:])
                return
            
            for i in range(start,n+1):
                lst.append(i)
                dfs(lst,i+1)
                lst.pop()


        dfs([],1)
        return res
         




#                                  dfs(3,1,[])
#                                  [1],[2],[3]
 
# dfs(5,2,[]). [1,2,3,4,5]
# [1,2],[1,3],[1,4],[1,5],[2,3],[3,4],[4,5],[2,5],and so on.
# from one element, explore all other possibilties.

#                 dfs([])
#             dfs([1]).   dfs([2]).   dfs([3])
#     dfs([1,2]),  dfs([1,3])
#  dfs([],)
#     dfs([1])
#         dfs([1,2]) -> return
#         dfs([1,3]) -> return


