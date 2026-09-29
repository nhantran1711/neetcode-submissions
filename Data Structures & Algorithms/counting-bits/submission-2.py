class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # 8 1000
        # 4 100
        # 2 010

        dp = [0] * (n + 1)
        # n = 5 = 4 + 1 
        for i in range(n + 1):
            dp[i] = (dp[i >> 1]) + (i & 1)
        return dp
