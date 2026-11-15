class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # does everybody trusts the same person?
        # if len(trust) >= n:
        #     return -1
        
        # is the second element of the nested list, same across the whole list?
        # using a map to see who person trusts who
        # map = {1:3, 4:3, 2:3}
        # sort it by key
        # {1:3,2:3,4:3}
        # loop through 1 - n values 
        # check if element in dict, if yes, check who it trusts, add it to lst
        # 
        # 1: [3,4]
        # 2: [3,4]
        # 4 : [3]
        # the town judge shoul not exist as a key, and should be present in the 
        # values of all the keys in dict.
        mp = {}
        for t in trust:
            p1,p2 = t[0],t[1]
            if p1 in mp:
                mp[p1].append(p2)
            else:
                mp[p1] = [p2]
        
        for person in range(n+1):
            if person not in mp:
                if all(person in value for value in mp.values()):
                    # found a town judge
                    return person
        
        return -1



             


    



