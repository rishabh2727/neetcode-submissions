class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        # keep track of days when price was less than current price
        # [100]
        # [100], current price is 80, so its only 1 return
        # [100,80], current price is 60, so add to stack (return 1)
        # [100,80,60] current price is 70, stack[-1] is 60,(return 1)
        # so we keep popping from stack till stack[-1] < current price
        # in this case, our days will be 2(return)
        # stack will be [100,80,70], current price is 75
        # pop again, days will be 2(return)
        # stack = [100,80,75], current price is 85
        # rather than using a variable days, I can use difference
        # in indexes of result and stack to find the span
        span = 1
        while self.stack and self.stack[-1][0] <= price:  
            # pop from stack, and record the number of days 
            stack_price, stack_span = self.stack.pop()
            span += stack_span

        self.stack.append([price,span])
        return span
# 

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)