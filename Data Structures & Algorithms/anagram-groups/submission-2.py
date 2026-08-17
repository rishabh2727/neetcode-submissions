class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        # {
        #     "act" : []
        #     if sorted("act") in my_dict
        #     then add the string to the list for that key
        # }
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in my_dict:
                my_dict[sorted_s].append(s)
            else:
                my_dict[sorted_s] = [s]
        
        res = []
        for v in my_dict.values():
            res.append(v)
        return res
        