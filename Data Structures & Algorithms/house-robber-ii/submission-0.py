class Solution:
    def check(self, nums):
        rob1 = rob2 = 0

        for n in nums:
            temp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = temp
        return rob2

    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.check(nums[1:]), self.check(nums[:-1]))