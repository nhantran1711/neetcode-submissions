class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = {0}

        for n in nums:
            nextDp = set()
            for t in dp:
                nextDp.add(t)
                nextDp.add(n + t)
            dp = nextDp
        return target in dp