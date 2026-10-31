class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # make two recursive calls, one with first element , one where you
        # skip it.

        def dfs(lst, position):

            if position == len(nums):
                res.append(lst[:])
                return
            lst.append(nums[position])
            dfs(lst,position+1)
            lst.pop()
            dfs(lst,position+1)

        
        dfs([],0)
        return res




# dfs([],0)
#     dfs([1],1)
#         dfs([1,2],2)
#             dfs([1,2,3],3)
#             res = [[1,2,3]] and return
#             lst = [1,2]
#             dfs([1,2],3)
#             res = [[1,2,3],[1,2]] and return
#             position = 2
#         dfs([1],2)
            # dfs([1,3],3)
            # res = [[1,2,3],[1,2],[1,3]] and return
            # dfs([1],3)
            # res = [[1,2,3],[1,2],[1,3],[1]] and return
        









        # [1].            []
        # [1,2].              [1]
        #                     [1,3]. [1]  
        # [1,2,3]. [1,2]

        # remember the position, rather than slicing and increasing TC
        # use index in the nums list

        # then return the set of res list.

        # base case? - if index == len(nums), return 
        # what do we return back from recursion? nothing

# help understand the patterns in backtracking, only the main ones I should familrize myself with. give 1-2 questions for each, how to have a very thorough understanding of it, so I dont get stuck. 

        

        