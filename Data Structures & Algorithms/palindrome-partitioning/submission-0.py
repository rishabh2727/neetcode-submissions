class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(string):
            l,r = 0,len(string)-1
            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True




        def dfs(index, temp):
            if index == len(s):
                res.append(temp[:])
                return
            
            for j in range(index,len(s)):
                sub_str = s[index:j+1]
                if isPalindrome(sub_str):
                    temp.append(sub_str)
                    dfs(j+1,temp)
                    temp.pop()
        
        dfs(0,[])
        return res




