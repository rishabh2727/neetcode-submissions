class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(lst, index):
            if index == len(nums):
                res.add(tuple(lst))
                return
            lst.append(nums[index])
            dfs(lst,index+1)
            lst.pop()
            dfs(lst,index+1)
        nums.sort()
        dfs([],0)
        return [list(s) for s in res]


# dfs([])
#     dfs([1],1)
#         dfs([1,2],2) 
#             dfs([1,2,1],3) -> return pop element from lst
#             dfs([1,2],3) -> return (index = 3) add to res pop element
#         dfs([1],2)
#             dfs([1,3],3) -> return 
#             dfs([1],3) -> return
