class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2

        dp = {0}
        for n in nums:
            newDp = set()
            for t in dp:
                newDp.add(t)
                newDp.add(n + t)
            dp = newDp
        return target in dp


        
