class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
# Think of the problem in three steps:
# 1. Convert the alien alphabet into something that tells you the position of each character.
# 2. Compare adjacent words character by character.
# 3. If the first different character in the first word comes after the corresponding character in the second word, return False.
        mp = {}
        for char in range(len(order)):
            mp[order[char]] = char
        print(mp)

# compare word 1 with word 2, then word 2 with word 3
        i,j = 0,1
        while j < len(words):
            word1 = words[i]
            word2 = words[j]
            print(word1,word2)
            c1, c2 = 0,0
            while c1 < len(word1) and c2 < len(word2):
                if mp[word1[c1]] > mp[word2[c2]]:
                    return False
                elif mp[word1[c1]] < mp[word2[c2]]:
                    break
                else:
                    c1 += 1
                    c2 += 1

            if c1 != len(word1) and c2 == len(word2):
                # word1 is longer than word2, so return False
                return False
            i += 1
            j += 1
        return True

                    



