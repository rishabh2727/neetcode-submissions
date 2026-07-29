from math import inf
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # finding number of boats
        # pick the first person in the array, try to pair him
        # up with someone. then cross them out, mark them complete.
        # do this for second and so on.


        # sort the array first, then the heaviest person will be
        # on right, and lighest person will be on left
        # if the heaviest cannot be paired with the lighest person
        # so it will have to be send in a single boat across.
        # move right pointer to the left.
        # so keep moving right pointer if pair not possible.

        # .sort() sorts the list in place — it modifies people directly
        #  — but it returns None
        people.sort()
        left = 0
        right = len(people)-1
        boats = 0
# [1,2,2,3,3]
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boats += 1
        
        return boats




        
