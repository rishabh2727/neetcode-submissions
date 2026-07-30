class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        # there is no point in doing left+1 here,
        # range(left+1, ) evalutes to 1, len(prices)
        # and this evaluation only happens once,
        # so when we do left = right, it does not change
        # the right's value
        for right in range(1,len(prices)):
            if prices[left] >= prices[right]:
                left = right
                continue
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        
        return max_profit
        
            








        