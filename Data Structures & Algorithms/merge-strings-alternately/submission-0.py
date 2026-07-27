class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        l1, l2 = 0,0
        r1, r2 = len(word1), len(word2)

        while l1 < r1 and l2 < r2:
            lst.append(word1[l1])
            lst.append(word2[l2])
            l1 += 1
            l2 += 1
        if l1 == r1:
            lst.append(word2[l2:r2])
        
        if l2 == r2:
            lst.append(word1[l1:r1])

        return "".join(lst)


        