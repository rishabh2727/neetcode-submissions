import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:

        # use max heap, and pop the char from heap.
        # c:3, d:2
        # pop a char, then make it unavailable for one iteration
        # heap = [(c,3), (d,2)]
        # c,d,c,d
        mp = {}
        for char in s:
            mp[char] = mp.get(char,0) + 1
        
        heap = []
        for key,val in mp.items():
            heapq.heappush(heap, (-val,key))
        
        # example heap = [(-2, 'y'), (-1, 'x'), (-1, 'a')]

        res = []
        temp_hold = []
        while heap:
            freq, character = heapq.heappop(heap)

            res.append(character)
            freq += 1

            if temp_hold:
                heapq.heappush(heap, temp_hold.pop())

            if freq < 0:
                temp_hold.append((freq, character))

        return "".join(res) if len(res) == len(s) else ""


        
        