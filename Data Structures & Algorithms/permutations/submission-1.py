class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def dfs(lst,mp):
            if len(lst) == len(nums):
                res.append(lst[:])
                return
            for i in range(len(nums)):
                # mark the element picked, and unavailable.
                # check if it is in dict, if yes then it is available
                if nums[i] in mp:
                    continue
                lst.append(nums[i])
                mp[nums[i]] = i
                dfs(lst,mp)
                lst.pop()
                mp.pop(nums[i])

        dfs([],{})
        return res



# for permutations, the length of all temp lsts we create is the same,
# at each recursive step we have three choices, we can choose either of all three
# elements given in nums. when nums = [1,2,3]
# dfs([],{})
#     dfs([1], {1})
#         dfs([1,2],{1,2})
#             dfs([1,2,3],{1,2,3}) -> return
#         dfs([1,3],{1,3})
#             dfs([1,3,2],{1,3,2}) -> return

#     dfs([2], {2})
#     dfs([3], {3})



            
            


        