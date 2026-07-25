class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        # even doing this, creates another string of length
        # N in memory, so try doing it using two pointers
        # s = s.lower()

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
                continue
            while left < right and not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
            
        
        return True




            
                
            


        # return s == s[::-1]

        