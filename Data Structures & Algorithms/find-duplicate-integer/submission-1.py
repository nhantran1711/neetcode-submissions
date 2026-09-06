class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        l, r = 0, n - 1 
        while l < r:
            m = (l + r) // 2
            sumLeft = sum(1 for num in nums if num <= m)

            if sumLeft <= m:
                l = m + 1
            else:
                r = m
        return l