class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        min_sub = nums[0]
        max_sub = nums[0]
        res = 0

        for n in nums[1:]:
            temp = [n, min_sub * n, max_sub * n]
            min_sub = min(temp)
            max_sub = max(temp)
            res = max(res, max_sub)
        return res