class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # any permutation of the string s1 should be there in
        # string 2, if yes then return true.
        # sliding window problem, beacuse we have to check 
        # the s1 in all places of s2, 
        # easy solution: we iterate throughh the string,
        # expand the window using the two pointers. once we
        # reach the window condition, we process it and check
        # if a permutation exists, if yes, we have the answer,
        # if no we contract the window, how to contract?
        # move the left and right by 1, it is fixed window size.

        l = 0
        size = len(s1)
        s1 = sorted(s1)
        for r in range(len(s2)):
            if r - l + 1 == size:
                if s1 == sorted(s2[l:r+1]):
                    return True
                else:
                    l += 1
        return False
            
    








        