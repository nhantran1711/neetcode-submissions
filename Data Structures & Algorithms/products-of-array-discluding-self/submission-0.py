class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)
        if n == 1:
            return nums
        
        pre = [1] * n 
        pre[0] = nums[0]

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i]
        
        suf = [1] * n
        suf[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i]

        res = [1] * n
        for i in range(n):
            if i == 0:
                res[i] = suf[i + 1]
            elif i == n - 1:
                res[i] = pre[i - 1]
            else:
                res[i] = pre[i - 1] * suf[i + 1]
        return res
            
