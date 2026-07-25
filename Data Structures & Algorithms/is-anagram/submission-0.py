class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        d = {}

        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        print(d)
        for char in t:
            if char not in d:
                return False
            else:
                if d[char] > 1:
                    d[char] -= 1
                else:
                    del d[char]
        
        return len(d) == 0
        # I can use hashmap, save every character with its frequency
        # , then check if all chars 

        # {
        # r : 2
        # a: 1
        # }
        # t =. carrace
        # for char in t:
        #     check char in dict
        #     if exists: 
        #         then reduce value by one
        #         if value is one, then remove the pair
        
        # last check if all values for all keys are 0
        # or just check if dict is empty




