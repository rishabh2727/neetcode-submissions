class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # prices = [7,1,5,3,6,4]
        # sell as you soon as you find a price higher
        # than buying price
        # if prices[left] < prices[right], good time to buy
        left = 0
        profit = 0
        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                # buy 
                curr_profit = prices[right] - prices[left]
                profit += curr_profit
            left = right
            
        return profit

            




        
