class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two pointers, left and right, while t not a substring
        # of s, keep adding char to our current string, 
        # we expand right until this condition, once it is
        # satisfied, we can try to shorten our window, by
        # moving left pointer +1, as long as t is a substring
        # of s
        t_mp = {}
        for char in t:
            t_mp[char] = t_mp.get(char,0) + 1
    
        left = 0
        cur_mp = {}
        shortest = float("inf")
        res = (-1,-1)
        for right in range(len(s)):
            # if characters in cur_string do not have all
            # characters from string t:
            # add s[right] to curr
            # check if x,y,z are all in curr
            # so maybe curr could be a dict, and lookups
            # would constant time
            # or just check if our curr dict contains all 
            # elements from t_mp
            cur_mp[s[right]] = cur_mp.get(s[right],0) + 1

            # remove char at left pointer, and keep 
            # removing until t is a substring
            # left += 1
            while self.contains_characters(cur_mp, t_mp):
                if (right-left+1) < shortest:
                    shortest = right-left+1
                    res = (left,right)
                cur_mp[s[left]] -= 1
                left += 1
        
            print(cur_mp)
        l,r = res
        return s[l:r+1] if shortest != float("inf") else ""        

    def contains_characters(self,cur_mp, t_mp):
        for char,count in t_mp.items():
            if cur_mp.get(char,0) < count:
                return False
        return True
            





        