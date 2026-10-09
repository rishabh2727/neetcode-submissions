import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = sorted(nums, reverse = True)
        # return nums[k-1]
        # do not sort it, so use priority queue
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
        
        # for i in range(k):
        #     heapq.heappop



        


        