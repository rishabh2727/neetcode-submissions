class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # what is the logic?
        # use two pointers, and for every day's temperature, we will 
        # have to check all future days, and find the earliest 
        # warmer day.
        # stack = []
        # now idea is to add the element in the stack, and unless
        # stack = [30]
        # use loop to add the cur element to stack
        # for i in range(0,len(temperatures)):
        #     stack = [temperatures[i]]
        #     while j < l
        # use a monotonic decreasing stack
        result = [0]* len(temperatures)
        stack = []

        # element is 30, stack is empty, so add.
        # stack = [30]
        # element is 38, check if element > stack[-1], we found 
        # warmer day. pop the topmost element from stack. update 
        # the result. then add the cur_element to stack.
        # we keep doing this if we find a larger element than stack[-1]
        # everytime. 
        # the other case is when element is smaller, we append it to the 
        # stack. since there is no warmer day found(larger element)


        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                Ind, Tem = stack.pop()
                result[Ind] = index - Ind

            stack.append((index,temp))

        return result


        

        # for i in range(0,len(temperatures)):
        #     cur_temp = temperatures[i]
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > cur_temp:
        #             result.append(j-i)
        #             break
        #     # if a warmer temp was not found, append 0
        #     if len(result) != i+1:
        #         result.append(0)
        
        # return result
                






        