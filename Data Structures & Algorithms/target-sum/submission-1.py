class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        



        dp = defaultdict(int)
        dp[0] = 0

        for num in nums:
            nextDp = defaultdict(int)

            for total, count in dp.items():
                nextDp[total + num] += count
                nextDp[total - num] -= count
            dp = nextDp
        return dp[target]
