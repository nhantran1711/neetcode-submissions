class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur, total = nums[0], nums[0]

        for i in range(1, len(nums)):
            cur = max(cur + nums[i], nums[i])
            total = max(total, cur)
        return total