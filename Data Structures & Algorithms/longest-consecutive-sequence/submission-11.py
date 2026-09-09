class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        seen = set(nums)
        res = 1

        for n in seen:
            if (n - 1) not in seen:
                length = 1
                num = n + 1
                while (num) in seen:
                    length += 1
                    res = max(res, length)
                    num += 1
        return res