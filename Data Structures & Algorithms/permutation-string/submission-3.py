class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # how to check if two string are permutation of each other
        mp = {}
        for char in s1:
            if char in mp:
                mp[char] += 1
            else:
                mp[char] = 1

        # is lec a permutation of s1(abc)?
        # is eca a permutation of s1(abc)?
        # is cab?
        # is abe? and so on ,
        # keep removing s2[left] from window, and add s2[right]
        # to the window.

        # now how to check elements between left and right?
        # add s2[right] to set until right-left+1 is equal to len(s1)

        # once length is equal, and elements have been added to set
        # we check if set(s1) == set(s2)
        print("S1_DICT:",mp)

        left = 0
        mp2 = {}
        for right in range(0,len(s2)):
            print("Iteration Number:", right)
            if s2[right] in mp2:
                mp2[s2[right]] += 1
            else:
                mp2[s2[right]] = 1
    #  s2="lecaabee"     
            print("S2_DICT:",mp2)
            if right-left+1 == len(s1):
                if mp2 == mp:
                    return True
                else:
                    mp2[s2[left]] -= 1
                    if mp2[s2[left]] == 0:
                        mp2.pop(s2[left])
                    left += 1


        return False






        



    








        