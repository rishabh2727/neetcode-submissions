import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
            # make two arrays separately, combine them depending
            # on which element is smaller, which should come first
            # when combining.
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1
                
            while j < len(right):
                result.append(right[j])
                j += 1

            return result
    
        return merge_sort(nums)





# [5,2,3,1]
# mergeSort(0,3), m = 1
#     mergeSort(0,1), m = 0
#         mergeSort(0,0) -> return
#         mergeSort(1,1) -> return
#         merge(l=0,m=0,r=1)
#     mergeSort(2,3), m = 2
#         mergeSort(2,2) -> return
#         mergeSort(3,3) -> return
#         merge(l=2,m=2,r=3)
#     merge(l=0,m=1,r=3)

