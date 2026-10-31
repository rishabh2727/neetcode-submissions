class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # keep taking more of one element means staying at the same index.
        # same pattern, of picking and not picking an element
        # nums = [2,5,6,9]
        def dfs(index,lst,target):
            if target == 0:
                res.append(lst[:])
                return
            if target < 0 or index == len(nums):
                return
            lst.append(nums[index])
            dfs(index,lst,target-nums[index])
            lst.pop()
            dfs(index+1,lst,target)
        
        dfs(0,[],target)
        return res
        

# dfs(0,[],9)
#     dfs(0,[2],7)
#         dfs(0,[2,2],5)
#             dfs(0,[2,2,2],3)
#                 dfs(0,[2,2,2,2],1)
#                     dfs(0,[2,2,2,2,2],-1) -> return
#                 dfs(1,[2,2,2,2],1)
#                     dfs(1,[2,2,2,2,5],-4) -> return
#                     dfs()

#     dfs(1,[],9)






