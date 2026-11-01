class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
# target = 8
# dfs(ind,target,[])
#     dfs(1,8-2=6,[2])
#         dfs(2,4,[2,2])
#             dfs(3,0,[2,2,4]) -> return
#             dfs(3,4,[2,2])
#                 dfs(4,-2,[2,2,6]) -> return
#                 dfs(4,4,[2,2])
#         dfs(2,6,[2])
#     dfs(1,8,[])

        res = []
        candidates.sort()
        def dfs(index,target,lst):
            if target == 0:
                res.append(lst[:])
                return
            if target < 0 or index == len(candidates):
                return
            lst.append(candidates[index])
            dfs(index+1,target-candidates[index],lst)
            lst.pop()
            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1

            dfs(index+1,target,lst)

        dfs(0,target,[])
        return res
      


        



    