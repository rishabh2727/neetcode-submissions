class FreqStack:

# priority queue

# maintain the stack order
# know the max frequency element



    def __init__(self):
        self.stack = []
        self.my_dict = {}

    def push(self, val: int) -> None:
        if val in self.my_dict:
            self.my_dict[val] += 1
        else:
            self.my_dict[val] = 1
        self.stack.append(val)

    def pop(self) -> int:
        # find the most frequent?
        # going through dict values, and picking the max
        max_frequency = max(self.my_dict.values())
        # find element in stack with this frequency, and pop it.
        # decrement its count in dict.iterate from end of stack 
        # so the element with that frequency which is close to top
        # of stack is removed.
        for i in range(len(self.stack)-1,-1,-1):
            if self.my_dict[self.stack[i]] == max_frequency:
                self.my_dict[self.stack[i]] -= 1
                return self.stack.pop(i)






      


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()