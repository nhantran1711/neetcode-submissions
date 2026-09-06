class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        seen = set(nums)
        res = 1

        for n in seen:
            
            if (n - 1) not in seen:
                length = 1             
                while (n + 1) in seen:
                    length += 1
                    n += 1
                res = max(res, length)
        return res



