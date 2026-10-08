import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]


        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones,(x-y))
        
        if len(stones) == 0:
            return 0

            
        return abs(stones[0])



        # add all elements of stones to heap,
        # length of heap will be 2,heap will be min heap until
        # # I add elements with negated values,
        # if you make heap of length 2, then add third element
        # to the heap and then pop it, becuase as soon as you add
        # the element heap arranges it on its own.





