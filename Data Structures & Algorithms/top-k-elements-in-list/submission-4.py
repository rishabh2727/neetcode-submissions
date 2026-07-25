class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}

        # O(n) to add all elements to dict
        for num in nums:
            my_dict[num] = 1 + my_dict.get(num,0)
        
        # make an array with key,value pair exactly like dict
        # but then sort it, so you can retrieve the top K
        
        # O(n) to add pair to array
        # I have to add it in this specific order, value,item
        # cause when I use sort, it sorts by first element
        arr = []
        for item,value in my_dict.items():
            arr.append([value, item])
        
        # O(nlogn) to use the built in sort method
        arr.sort()
        print(arr)

        result = []
        # how to retrieve element from dict with highest values
        # O(k) to add top K to result
        while len(result) < k:
            result.append(arr.pop()[1])

        return result



# total TC = O(nlogn)
# total SC = O(n)
            





        
