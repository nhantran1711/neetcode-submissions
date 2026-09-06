class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = -prices[0]
        hold = 0

        for i in range(1, len(prices)):
            hold = max(hold, buy + prices[i])
            buy = max(buy, -prices[i])
        return hold
