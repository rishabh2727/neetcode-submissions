class MyQueue:

# using two stacks, 
# first in first out.
# 1,2,3
# 3,2,1
# stack = [2]
# stack2 = [3,1,2]
# stack = [2,1,3]
# stack2 = [3,]


    def __init__(self):
        self.stack = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)


    def pop(self) -> int:
        if not self.stack2:
            while self.stack:
                element = self.stack.pop()
                self.stack2.append(element)
        return self.stack2.pop()

        
    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack:
                element = self.stack.pop()
                self.stack2.append(element)
        return self.stack2[-1]

        

    def empty(self) -> bool:
        return max(len(self.stack2), len(self.stack)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()