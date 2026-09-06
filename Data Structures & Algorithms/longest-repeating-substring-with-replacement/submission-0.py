class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        


        l = 0
        counter = {}
        res = 0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1

            while (r - l + 1 ) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            
        return res
