class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen = set(nums)
        res = 1

        for n in seen:
            length = 1
            while (n + 1) in seen:
                length += 1
                res = max(res, length)
                n += 1
        return res