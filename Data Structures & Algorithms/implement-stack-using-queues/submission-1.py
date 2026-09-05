from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()


    # we have one main and one helper queue
    # helper queue only stores one element, and all other
    # elements in main are appended behind it, so it is exactly
    # like a stack, then we swap the queues, so the helper 
    # becomes empty again, and the main has the original order
    # of a stack, basically reversed order.
    def push(self, x: int) -> None:
        self.q1.append(x)
        for _ in range(len(self.q1)-1):
            element = self.q1.popleft()
            self.q1.append(element)
        
    def pop(self) -> int:
        return self.q1.popleft()
        

    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()