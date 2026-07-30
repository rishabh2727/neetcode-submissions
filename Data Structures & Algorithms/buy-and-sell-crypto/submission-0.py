class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if right < left, always better to buy at right
        # move the left pointer there, and right will be left +1
        # always try to follow through on example, see what reasoning
        # and logic is there, code is last
        # when nums[left] >= nums[right]:
        # left = right
        # right += 1
        # else:
        #     right += 1
        [10,1,5,6,7,1]

        left = 0
        max_profit = 0
        for right in range(left+1,len(prices)):
            if prices[left] >= prices[right]:
                left = right
                continue
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        
        return max_profit
        
            








        