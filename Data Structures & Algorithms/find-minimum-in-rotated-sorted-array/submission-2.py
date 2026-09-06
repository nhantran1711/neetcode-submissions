class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        res = float('inf')
        l, r = 0, len(nums) - 1

        while l <= r:

            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                return res
            
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                res = min(res, nums[m])
                l = m + 1
            else:
                res = min(res, nums[m])
                r = m - 1
        return res