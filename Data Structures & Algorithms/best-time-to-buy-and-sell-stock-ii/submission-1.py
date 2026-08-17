class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,1


        if len(prices) <= 1:
            return 0

        # [1,5,8,9,14]
        profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit += prices[sell] - prices[buy]
            buy += 1
            sell += 1
        return profit




        