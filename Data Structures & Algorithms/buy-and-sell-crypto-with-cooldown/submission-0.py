class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        dp = {} # (i, isBuying) : max_val


        def dfs(i, isBuying):
            if i >= len(prices):
                return 0
            
            if (i, isBuying) in dp:
                return dp[(i, isBuying)]
            
            if isBuying:
                bought = dfs(i + 1, not isBuying) - prices[i]
                cooldown = dfs(i + 1, isBuying)
                dp[(i, isBuying)] = max(bought, cooldown)
            else:
                sell = dfs(i + 2, not isBuying) + prices[i]
                cooldown = dfs(i + 1, isBuying)
                dp[(i, isBuying)] = max(sell, cooldown)

            return dp[(i, isBuying)]
        return dfs(0, True)
            