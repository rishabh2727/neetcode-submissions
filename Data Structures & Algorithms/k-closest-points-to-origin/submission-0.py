import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # simplify the question.
        # points = [3,2,1,5]
        # find 2 points closest to zero.
        # finding the min 2 points
        # so I will go through the array, and add it to a heap
        x2 = 0
        y2 = 0
        heap = []
        lst = []
        for coordinates in points:
            x1 = coordinates[0] 
            y1 = coordinates[1]
            distance = (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
            heapq.heappush(heap, (distance, coordinates))
        
        # closest point will have the shortest distance, our heap
        # is sorted by the distance, the top element is smallest
        # we pop k times
        for i in range(k):
            distance, coordinates = heapq.heappop(heap)
            lst.append(coordinates)

        return lst

        # this is O(nlogn for first loop and then O(k log n for second
        # loop) total time complexity would be O(nlogn)
        # and SC = O(n) + O(n) = O(n)

        # we can further optimize this by using a max heap
        # this way the points we want to remove are at the top
        # and we can pop when len(heap) > k.
        # so we are left with k smallest/closest points
