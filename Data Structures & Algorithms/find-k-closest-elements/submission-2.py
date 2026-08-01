class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lst = []
        for n in arr:
            lst.append(abs(n-x))
        
        print(lst)

        res = []
        # from this lst array, save the top k elements
        # which pass the conditions
        # [4, 2, 1, 2]

        best = float("inf")
        best_index = -1
        while k:
            for i,val in enumerate(lst):
                if val>=0 and val < best:
                    best = val
                    best_index = i
            res.append(arr[best_index])
            lst[best_index] = -1
            best = float("inf")
            
            k -= 1

        res.sort() 
        return res
            