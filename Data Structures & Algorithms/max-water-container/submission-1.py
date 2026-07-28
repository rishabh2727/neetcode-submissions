class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maxarea = 0
        # for i in range(0, len(heights)):
        #     for j in range(i+1, len(heights)):
        #         container_area = (j-i)*(min(heights[i],heights[j]))
        #         print(container_area)
        #         maxarea = max(container_area, maxarea)
        
        # return maxarea

        # only loop through the array once. two pointers
        # at the end of the array
        i = 0
        j = len(heights)-1
        maxarea = 0

        while i < j:
            container_area = (j-i)*(min(heights[i],heights[j]))
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
            maxarea = max(maxarea, container_area)
        
        return maxarea
            
            




        
        