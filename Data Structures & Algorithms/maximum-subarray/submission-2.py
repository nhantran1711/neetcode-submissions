class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        cur, total = nums[0], nums[0]

        for n in nums[1:]:
            cur = max(n, cur + n)
            total = max(total, cur)
        return total


