class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        # s="abc"
        while left < right:
            if s[left] != s[right]: 
            # check two possibilities
                skipL = s[left+1:right+1]
                skipR = s[left:right]
                return skipL == skipL[::-1] or skipR == skipR[::-1]

            left += 1
            right -= 1

        return True


        



        
       



        