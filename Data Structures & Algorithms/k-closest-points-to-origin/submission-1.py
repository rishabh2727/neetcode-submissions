import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        # distance is smallest, 
        # max heap
        # 2.5, 1.7, 6,8, 2.9   2 closest points
        # 2.5, 1.7,
        # so we need max heap, add points to heap, if length exceeds
        # k, pop the point from the heap.
        heap = []
        x2,y2 = 0,0
        for p in points:
            x1,y1 = p[0],p[1]
            dist = (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
            heapq.heappush(heap,(-dist,[x1,y1]))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for pair in heap:
            coordinate = pair[1]
            res.append(coordinate)
        return res









