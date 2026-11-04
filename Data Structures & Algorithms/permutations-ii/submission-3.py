class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    # nums = [1,1,2]
    # # in this case, map would not work, since there are duplicates.

    #     put all elements int othe 
    # dfs([],{1:2,2:1})
    #     dfs([1],{1:1,2:1})
    #         dfs([1,1],{2:1})
    #             dfs([1,1,2],{}) -> dict is empty, all elements taken, then add to res
    #     dfs([1])

    #     dfs([2])
        mp = {}
        for n in nums:
            mp[n] = mp.get(n,0) + 1

        res = []
        
        def dfs(lst,my_dict):
            if all(value==0 for value in my_dict.values()):
                res.append(lst[:])
                return
            for key in my_dict:
                if my_dict[key] < 1:
                    continue
                lst.append(key)
                my_dict[key] -= 1
                dfs(lst,my_dict)
                lst.pop()
                my_dict[key] += 1

        
        dfs([],mp)
        return res


    





        

        